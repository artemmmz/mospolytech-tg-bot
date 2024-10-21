""" Module for an invalid argument error class """


class InvalidArgumentError(Exception):
    """
    Exception raised when an invalid argument is passed.
    """

    def __init__(self, argument_name: str):
        """

        :param argument_name: Argument name for send it somewhere
        """
        super().__init__()
        self.argument_name = argument_name
