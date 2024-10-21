""" Module for a schedule error class """


class ScheduleError(Exception):
    """
    Exception raised when schedule or arguments
    for schedule contains errors
    """

    def __init__(self, message):
        """
        Initialization method

        :param message: Message to display
        """
        self.message = message
