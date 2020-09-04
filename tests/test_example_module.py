import unittest

from {{library_name}} import exceptions, ExampleModule

from .base import BaseTestCase


class TestExampleModule(BaseTestCase):
    """ Testing operation of the ExampleModule class
     """

    def test_init_example_module(self):
        """ Ensures that the twine class can be instantiated with a file
        """
        test_data_file = self.path + "test_data/.json"
        ExampleModule()


if __name__ == "__main__":
    unittest.main()
