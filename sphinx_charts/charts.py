import os
import posixpath
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.utils import relative_path
from pkg_resources import resource_filename
from sphinx.util import logging
from sphinx.util.osutil import copyfile, ensuredir


logger = logging.getLogger(__name__)


FILES = [
    "plotly/plotly-2.11.1.min.js",
    "charts.css",
    "charts.js",
]


DEFAULT_DOWNLOAD_NAME = "chart"


def get_compatible_builders(app):
    # TODO Add PDF to builders (using a rendered png)
    builders = [
        "html",
        "singlehtml",
        "dirhtml",
        "readthedocs",
        "readthedocsdirhtml",
        "readthedocssinglehtml",
        "readthedocssinglehtmllocalmedia",
    ]
    return builders


def _clean_px_value(argument):
    return directives.length_or_percentage_or_unitless(argument, "px")


def _clean_download_name_value(argument):
    if argument.endswith(".svg"):
        return argument.replace(".svg", "")
    return directives.unchanged(argument)


class ChartDirective(Directive):
    """Top-level chart directive"""

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True

    option_spec = {
        # TODO allow static images for PDF renders   'altimage': directives.unchanged,
        "height": _clean_px_value,
        "width": _clean_px_value,
        "download_name": _clean_download_name_value,
    }

    def run(self):
        """Parse a plotly chart directive"""
        self.assert_has_content()
        env = self.state.document.settings.env

        # Ensure the current chart ID is initialised in the environment
        if "next_chart_id" not in env.temp_data:
            env.temp_data["next_chart_id"] = 0

        # Get the ID of this chart
        id = env.temp_data["next_chart_id"]

        # Handle the src and destination URI of the *.json asset
        uri = directives.uri(self.arguments[0].strip())
        src_uri = os.path.join(env.app.builder.srcdir, uri)  # Where to get the asset during build
        build_uri = os.path.join(env.app.builder.outdir, "_charts", uri)  # Where to put the asset during build
        page_uri = os.path.join(env.app.builder.outdir, env.docname)  # The location of the current page
        relative_uri = relative_path(page_uri, build_uri)  # Ultimate path of the asset relative to current page

        # Create the main node container and store the URI of the file which will be collected later
        node = nodes.container(id="ffs")
        node["classes"] = ["sphinx-charts"]

        # Increment the ID counter ready for the next chart
        env.temp_data["next_chart_id"] += 1

        # Only if its a supported builder do we proceed (otherwise return an empty node)
        if env.app.builder.name in get_compatible_builders(env.app):

            # Make the directories and copy file (if file has changed)
            ensuredir(os.path.dirname(build_uri))
            copyfile(src_uri, build_uri)

            download_name = self.options.pop("download_name", DEFAULT_DOWNLOAD_NAME)
            chart_node = nodes.container()
            chart_node["classes"] = [
                "sphinx-charts-chart",
                f"sphinx-charts-chart-id-{id}",
                f"sphinx-charts-chart-uri-{relative_uri}",
                f"sphinx-charts-chart-dn-{download_name}",
            ]
            chart_node.replace_attr("ids", [f"sphinx-charts-chart-id-{id}"])

            # This is a botch. Purely here to force inclusion of mathjax on pages with charts but without latex in the
            # document, because it doesn't find the $$ in the chart data (which isn't part of the document tree)
            math_node = nodes.paragraph("$$", "")
            math_node["classes"] = ["sphinx-charts-hidden"]

            placeholder_node = nodes.container()
            placeholder_node["classes"] = ["sphinx-charts-placeholder", f"sphinx-charts-placeholder-{id}"]
            placeholder_node += nodes.caption("", "Loading...")

            node += chart_node
            node += math_node
            node += placeholder_node

            # Add optional chart caption and legend (as per figure directive)
            if self.content:
                caption_node = nodes.Element()  # Anonymous container for parsing
                self.state.nested_parse(self.content, self.content_offset, caption_node)
                first_node = caption_node[0]
                if isinstance(first_node, nodes.paragraph):
                    caption = nodes.caption(first_node.rawsource, "", *first_node.children)
                    caption.source = first_node.source
                    caption.line = first_node.line
                    node += caption
                elif not (isinstance(first_node, nodes.comment) and len(first_node) == 0):
                    error = self.state_machine.reporter.error(
                        "Chart caption must be a paragraph or empty comment.",
                        nodes.literal_block(self.block_text, self.block_text),
                        line=self.lineno,
                    )
                    return [node, error]
                if len(caption_node) > 1:
                    node += nodes.legend("", *caption_node[1:])

        return [node]


class _FindChartDirectiveVisitor(nodes.NodeVisitor):
    """Visitor pattern than looks for a :: chart directive in a document"""

    def __init__(self, document):
        nodes.NodeVisitor.__init__(self, document)
        self._found = False
        self.charts = []

    def unknown_visit(self, node):
        if (
            not self._found
            and isinstance(node, nodes.container)
            and "classes" in node
            and isinstance(node["classes"], list)
        ):
            self._found = "sphinx-charts" in node["classes"]
        if isinstance(node, nodes.container) and "sphinx_charts_json_uri" in node:
            self.charts.append(node["sphinx_charts_json_uri"])

    @property
    def found_plotly_chart_directive(self):
        """Return whether a sphinx plotly chart directive was found"""
        return self._found


def update_context(app, pagename, templatename, context, doctree):
    """Remove CSS and JS asset files if no charts are used"""
    if doctree is None:
        return
    visitor = _FindChartDirectiveVisitor(doctree)
    doctree.walk(visitor)
    if not visitor.found_plotly_chart_directive:
        paths = [posixpath.join("_static", "sphinx_charts/" + f) for f in FILES]
        if "css_files" in context:
            context["css_files"] = context["css_files"][:]
            for path in paths:
                if path.endswith(".css") and path in context["css_files"]:
                    context["css_files"].remove(path)
        if "script_files" in context:
            context["script_files"] = context["script_files"][:]
            for path in paths:
                if path.endswith(".js") and path in context["script_files"]:
                    context["script_files"].remove(path)


def copy_assets(app, exception):
    """Copy asset files to the output"""
    if "getLogger" in dir(logging):
        log = logging.getLogger(__name__).info
        warn = logging.getLogger(__name__).warning
    else:
        log = app.info
        warn = app.warning
    builders = get_compatible_builders(app)
    if exception:
        return
    if app.builder.name not in builders:
        if not app.config["sphinx_charts_nowarn"]:
            warn(f"Not copying plotly assets! Not compatible with {app.builder.name} builder")
        return

    log("Copying sphinx_charts plotly js and css assets")

    installdir = os.path.join(app.builder.outdir, "_static", "sphinx_charts")

    for path in FILES:
        source = resource_filename("sphinx_charts", path)
        dest = os.path.join(installdir, path)
        destdir = os.path.dirname(dest)
        if not os.path.exists(destdir):
            os.makedirs(destdir)

        copyfile(source, dest)


def setup(app):
    """Set up the plugin"""
    app.add_config_value("sphinx_charts_nowarn", False, "")
    app.add_config_value("sphinx_charts_valid_builders", [], "")
    app.add_directive("chart", ChartDirective)

    # Add the mathjax js file above plotly
    # TODO remove this hack once
    #  https://stackoverflow.com/questions/63745272/ordering-of-javascript-scripts-in-head-when-using-sphinx-ext-mathjax
    #  is answered
    # For some reason mathjax configures itself with defaults, then the custom configuration is only changed at the end,
    # so any value of 'mathjax_path' specified in conf.py isn't seen here. Sigh.
    configured_mathjax_path = getattr(app.config, "mathjax_path", None)
    smd_defined_mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
    svg_mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-svg.js"

    if (configured_mathjax_path is not None) and ("TeX-AMS-MML_HTMLorMML" in configured_mathjax_path):
        # Warn on use of v2 mathjax used by older sphinx_math_dollar versions
        svg_mathjax_path = smd_defined_mathjax_path.replace("TeX-AMS-MML_HTMLorMML", "TeX-AMS-MML_SVG")
        logger.warning(
            "The mathjax path defined in your conf.py (or by your version of sphinx-math-dollar) uses an old v2 version of mathjax, incompatible with the present version of plotly. Charts featuring LaTex, or LaTeX symbols in your text, may render incorrectly."
        )

    elif (configured_mathjax_path is not None) and (configured_mathjax_path == smd_defined_mathjax_path):
        # Account for v3 of mathjax used by newer sphinx_math_dollar versions
        logger.info(
            f"Plotly requires an SVG renderer for LaTeX elements, not an HTML renderer. Adding {svg_mathjax_path}."
        )

    elif configured_mathjax_path is None:
        logger.info(f"Plotly requires mathjax. Adding {svg_mathjax_path}.")

    else:
        raise ValueError(
            "Could not update the mathjax_path used by sphinx_math_dollar - perhaps your version of sphinx_math_dollar is incompatible with sphinx_charts? Raise an issue on the sphinx_charts github page to get help!"
        )

    app.add_js_file(svg_mathjax_path)

    for path in ["sphinx_charts/" + f for f in FILES]:
        if path.endswith(".css"):
            if "add_css_file" in dir(app):
                app.add_css_file(path)
            else:
                app.add_stylesheet(path)
        if path.endswith(".js"):
            if "add_script_file" in dir(app):
                app.add_script_file(path)
            else:
                try:
                    app.add_js_file(path)
                except AttributeError:
                    # For backward compatibility with Sphinx 2 and 3
                    app.add_javascript(path)

    app.connect("html-page-context", update_context)
    app.connect("build-finished", copy_assets)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
