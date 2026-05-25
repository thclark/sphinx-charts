import unittest

from sphinx_charts.charts import ChartDirective  # noqa
from sphinx_charts.charts import _get_svg_mathjax_path
from .base import BaseTestCase


class TestExampleModule(BaseTestCase):
    """Testing operation of the ExampleModule class"""

    def test_placeholder(self):
        """Just a placeholder"""
        pass


class TestMathJaxPath(BaseTestCase):
    """Testing mathjax path handling"""

    def test_sphinx_mathjax_v3_chtml_path_uses_svg_renderer(self):
        """Sphinx MathJax v3 CHTML paths are converted to SVG paths"""
        assert _get_svg_mathjax_path(
            "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
        ) == "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-svg.js"

    def test_sphinx_mathjax_v4_chtml_path_uses_svg_renderer(self):
        """Sphinx MathJax v4 CHTML paths are converted to SVG paths"""
        assert _get_svg_mathjax_path(
            "https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"
        ) == "https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-svg.js"

    def test_custom_chtml_path_uses_matching_svg_renderer(self):
        """Custom CHTML component paths are converted to their SVG equivalent"""
        assert _get_svg_mathjax_path("/static/mathjax/tex-chtml.js") == "/static/mathjax/tex-svg.js"


if __name__ == "__main__":
    unittest.main()
