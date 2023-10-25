import typing

from . import at

T = typing.TypeVar("T")
S = typing.TypeVar("S")


def find(func: typing.Callable[..., bool], L: typing.Iterable[T]) -> T | None:
    for e in filter(func, L):
        return e

    return None


class Iterator(typing.Iterable[T]):
    """
    Iterator([1,2,3]).map(lambda x: x**2).filter_by(2).eval() => [4]
    のような感じで使えるイテレータークラス
    """

    def __init__(self, it: typing.Iterable[T]):
        self.it = iter(it)

    def eval(self) -> list[T]:
        return list(self)

    def __next__(self) -> T:
        return next(self.it)

    def __iter__(self) -> typing.Iterator[T]:
        return self.it

    def map(self, func: typing.Callable[[T], S]) -> "Iterator[S]":
        return Iterator(map(func, self))

    def filter(self, func: typing.Callable[..., bool]) -> "Iterator[T]":
        return Iterator(filter(func, self))

    def filter_by(self, value: T) -> "Iterator[T]":
        return self.filter(lambda x: x == value)

    def find(self, func: typing.Callable[..., bool]) -> T | None:
        v = find(func, self)

        if v is None:
            return None

        return v

    def find_by(self, value: T) -> T | None:
        return self.find(lambda x: x == value)

    def at(self, func: typing.Callable[..., bool]) -> at[T]:
        v = self.find(func)

        if v is None:
            raise ValueError("No value found")

        return at(v)

    def at_by(self, value: T):
        return self.at(lambda x: x == value)
