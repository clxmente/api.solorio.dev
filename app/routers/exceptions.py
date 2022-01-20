class DoesNotExist(Exception):
    pass

class PasswordNotLongEnough(Exception):
    def __init__(self, length: int) -> None:
        self.length = length

class PasswordTooLong(Exception):
    def __init__(self, length: int) -> None:
        self.length = length

class ExcludedAllSets(Exception):
    pass