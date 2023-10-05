from enum import Enum, auto


class Base(Enum):
    def lower(self):
        return self.name.lower()

    def from_name(name: str):
        return Base[name.upper()]
