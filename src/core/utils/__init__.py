import typing

T = typing.TypeVar("T")
S = typing.TypeVar("S")


class If:
    def __init__(self, statement: typing.Callable[[], bool]):
        self.__statements = [statement]
        self.__calls: list[typing.Callable] = []

    def ElseIf(self, statement: typing.Callable[[], bool]):
        self.__statements.append(statement)
        return self

    def Else(self, func: typing.Callable):
        self.__statements.append(lambda: True)
        self.__calls.append(func)
        return self

    def then(self, func: typing.Callable):
        self.__calls.append(func)
        return self

    def end(self):
        for i, statement in enumerate(self.__statements):
            if statement():
                return self.__calls[i]()

        return None


class at(typing.Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def __call__(self):
        return self.value

    def then(self, func: typing.Callable[[T], S]) -> "at[S]":
        return at(func(self.value))

    def If(self, statement: typing.Callable[[T], bool]) -> If:
        return If(lambda: statement(self.value))
