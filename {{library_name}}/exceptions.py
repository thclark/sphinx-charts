

class ExampleModuleException(Exception):
    """ All exceptions raised by the library inherit from this exception
    """


class SomethingException(ExampleModuleException):
    """ Raised when the code throws its toys out of the pram
    """

