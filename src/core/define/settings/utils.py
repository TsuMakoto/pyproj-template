from typing import Generic, TypeVar

T = TypeVar('T')


class __Const(Generic[T]):
    def __init__(self, id_: int, val: T):
        self.id = id_
        self.val = val

    def __eq__(self, other):
        return self.id == other.id and self.val == other.val

    def __hash__(self):
        return hash((self.id, self.val))


class __Consts:
    def __init__(self):
        self.id = 0

    def __call__(self, val: T) -> __Const[T]:
        self.id += 1
        return __Const(self.id, val)


consts = __Consts()


__all__ = ['consts']
