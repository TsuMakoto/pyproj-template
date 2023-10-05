from typing import Generic, TypeVar

T = TypeVar('T')


class Const(Generic[T]):
    def __init__(self, id_: int, val: T):
        self.id = id_
        self.val = val

    def __eq__(self, other):
        return self.id == other.id and self.val == other.val

    def __hash__(self):
        return hash((self.id, self.val))


if __name__ == "__main__":
