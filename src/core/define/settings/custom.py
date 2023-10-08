# from typing import NamedTuple
# from .consts import Const
# from .consts import const
from .consts import Consts as _Consts
from .consts import Structs as _Structs
from .enums import Enums as _Enums


class Structs(_Structs):
    pass


class Consts(_Consts):
    pass


class Enums(_Enums):
    pass


__all__ = ['Consts',  'Enums']
