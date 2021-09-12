from dataclasses import dataclass


@dataclass
class MovieError(Exception):

    error_code: int
    error_message: str
    error_details: str

    def __init__(self, error_code, error_message, error_details=None):
        self.error_code = error_code
        self.error_message = error_message
        self.error_details = error_details
        super().__init__(error_message)
