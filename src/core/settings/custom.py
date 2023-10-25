from .enums import Enum
from .enums import enums as base

"""
独自定数がある場合は、ここに記載
使うときは、
from src.core.settings.enums import enums
の代わりに
from src.core.settings.custom import enums
を使う
"""


class enums(base):
    class MyConsts(Enum):
        pass
