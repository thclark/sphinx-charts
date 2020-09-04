import logging
import pkg_resources

from . import exceptions


logger = logging.getLogger(__name__)


EXAMPLE_CONSTANT = 2

EXAMPLE_CONSTANT_OPTIONS = (
    "a_value",
    "another_value",
)


class ExampleModule:
    """ Some documentation about the class.

    It'll get rendered in the auto generated docs. If Kanye could see this he'd rap about how great it is.

    """
    def __init__(self, **kwargs):
        """ Instantiate a glorious ExampleModule
        """
        pass

    def _example_private_method(self):
        """ Does private things not for use outside the library

        As indicated by preceding its name with _

        """
        pass

    def example_method(self, example_arg, example_kwarg=None):
        """ A public method to show parameter stuff in docstrings

        :param example_arg: Document the function parameter
        :param example_kwarg: Document the function parameter
        :return: None

        """

    def example_error_handling_and_logging(self, thing):
        """ Method to show how to handle an error
        """
        try:
            logger.debug("Doing something to a thing (thing: %s)", thing)
            do_something(thing, EXAMPLE_CONSTANT, EXAMPLE_CONSTANT_OPTIONS)

        except NameError as e:
            raise exceptions.SomethingException(str(e))

    def example_of_how_to_refer_to_a_file_in_the_package(self):
        """ Method showing how to reference files within the package

        You need to refer to the file in the package bundle, because you don't know where the
        module will be called from... this gets you the right path always, relative to {{library_name}}

        Don't forget to include non-python files in the MANIFEST.in too!

        """
        file_name = pkg_resources.resource_string("{{library_name}}", "module_data/file_required_by_module.json")
        logger.info("file name is %s", file_name)
