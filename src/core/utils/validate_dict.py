"""
d = {
    "a": {
        "b": {
            "c": {
                "d": "hoge"
            }
        },
        "x": {
            "y": {
                "z": "fuga"
            }
        }
    }
}

があったときに、キーの存在検証と、型チェックを以下の形で行う。

with ValidateDict(d) as vd:
    with vd("a") as vda:
        with vda("b") as vdb:
            with vdb("c") as vdc:
                assert vdc("d", str)

        with vda("x") as vdx:
            with vdx("y") as vdy:
                assert vdy("z", str)
"""

import re
from typing import Mapping, Type


class ValidateDict(Mapping):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def forall(self, key: str):
        if key not in self:
            raise KeyError(f"Key '{key}' is not found.")

        d = self[key]

        if not isinstance(d, list):
            raise TypeError(f"Key '{key}' is not instance of 'list'.")

        validates: list["ValidateDict"] = []
        for e in d:
            if not isinstance(e, dict):
                raise TypeError(f"Key '{key}' is not instance of 'TypedDict'.")
            else:
                validates.append(ValidateDict(**e))
        return validates

    def __call__(self, key: str):
        if key not in self:
            raise KeyError(f"Key '{key}' is not found.")

        d = self[key]

        if isinstance(d, list):
            raise TypeError(f"Key '{key}' is instance of 'list'. Use 'forall' method.")

        elif not isinstance(d, dict):
            raise TypeError(f"Key '{key}' is not instance of 'TypedDict'.")

        return ValidateDict(**d)

    def is_valid(self, key: str, type_: Type):
        if key not in self:
            return False, f"Key '{key}' is not found."

        if not isinstance(self[key], type_):
            return False

        return True

    def validate(
        self,
        key: str,
        type_or_literal: Type | list,
        fmt: str = "",
        cast_type=(lambda x: x),
    ):
        if key not in self:
            raise KeyError(f"Key '{key}' is not found.")

        d = self[key]

        if isinstance(type_or_literal, list):
            if d not in type_or_literal:
                raise ValueError(f"Value '{d}' is not include in '{type_or_literal}'.")
        else:
            if not isinstance(d, type_or_literal):
                raise TypeError(
                    f"Key '{key}' is not instance of '{type_or_literal.__name__}'."
                )

        if isinstance(d, list | dict):
            return d

        if fmt != "":
            if not re.match(fmt, str(d)):
                raise ValueError(f"Value '{d}' is not match with '{fmt}'.")

        self.d[key] = cast_type(d)  # type: ignore

        return self[key]

    def __getitem__(self, key: str):
        return self[key]

    def __setitem__(self, key: str, value):
        self.d[key] = value  # type: ignore
