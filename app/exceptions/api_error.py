""" Module with API exception """


class APIError(Exception):
    """
    Exception raised when an MosPolytech API request fails.
    """

    def __init__(self, message):
        """
        Method for initialization APIError.

        :param message: Error message
        """
        super().__init__(message)
        self.message = message
