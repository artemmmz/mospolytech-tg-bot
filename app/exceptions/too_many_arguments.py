class TooManyArgumentsError(Exception):
    def __init__(self, needed_arguments: int, given_arguments: int):
        self.needed_arguments = needed_arguments
        self.given_arguments = given_arguments
        super().__init__()
