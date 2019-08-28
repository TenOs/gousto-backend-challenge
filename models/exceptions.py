

class GoustoBaseException(Exception):
    """
    Base exception for the project.

    All exceptions thrown should be of this type, and will then be caught
    by the error handler and will be correctly formatted.

    Attributes:
        id              id of the exception, by default it will be
                        the class name
        code            http status code to return
        description     error message displayed to the user
    """
    id: str
    code: int
    description: str

    def __init__(self, *args: object) -> None:
        """
        Initializes a new Instance
        :param args:
        """
        super().__init__(*args)
        self.id = self.__class__.__name__
        self.code = self.__getattribute__('code') or 400


class RecipeNotFoundException(GoustoBaseException):
    """
    This exception should be thrown when a Recipe is not found,
    """
    code = 404
    description = 'The recipe is not found'
