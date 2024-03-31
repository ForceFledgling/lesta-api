class UnicornException(Exception):
    def __init__(self, msg: str):
        self.msg = msg
        super().__init__(msg)  # passing an error message to the base Exception class
