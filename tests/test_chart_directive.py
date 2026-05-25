import unittest

from sphinx_charts.charts import ChartDirective  # noqa
from sphinx_charts.charts import _remove_static_asset
from .base import BaseTestCase


class StaticAsset:
    def __init__(self, filename):
        self.filename = filename


class TestExampleModule(BaseTestCase):
    """Testing operation of the ExampleModule class"""

    def test_placeholder(self):
        """Just a placeholder"""
        pass


class TestStaticAssetRemoval(BaseTestCase):
    """Testing Sphinx static asset cleanup"""

    def test_removes_string_asset_paths(self):
        """String asset paths are removed from the context"""
        assets = ["_static/sphinx_charts/charts.css", "_static/theme.css"]

        assert _remove_static_asset("_static/sphinx_charts/charts.css", assets) == ["_static/theme.css"]

    def test_removes_sphinx_static_asset_objects(self):
        """Sphinx static asset objects are matched by filename"""
        chart_asset = StaticAsset("_static/sphinx_charts/charts.js")
        theme_asset = StaticAsset("_static/theme.js")

        assert _remove_static_asset("_static/sphinx_charts/charts.js", [chart_asset, theme_asset]) == [theme_asset]


if __name__ == "__main__":
    unittest.main()
