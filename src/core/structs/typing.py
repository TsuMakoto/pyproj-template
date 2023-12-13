import re
from typing import Callable, Generic, Literal, NamedTuple, TypeVar, cast

import typing_extensions as tx

# ----------------------------------------
# Raw dataやAPI json, 設定ファイルなどの型定義などしたい場合はここに
# ここは構造体のみ記載して、実装したい場合は、./implに記載する
# ----------------------------------------

num_type = int | float
eq_type = Literal["<", "<=", "==", ">=", ">"]
SchemaType = TypeVar("SchemaType", int, float, str, bool)
DataType = TypeVar("DataType")


class typing:
    class Vector2D(NamedTuple):
        x: float
        y: float

        def __str__(self):
            return f"({self.x}, {self.y})"

    class Geometry(NamedTuple):
        lat: float
        lon: float

    class Schema:
        class Error(NamedTuple):
            row: int
            msg: str

            def __str__(self):
                if self.row == 0:
                    return f"Header: {self.msg}"
                else:
                    return f"row number[{self.row}]: {self.msg}"

        class Schema(tx.NamedTuple, Generic[SchemaType, DataType]):
            ID: int
            name: str
            short_description: str
            T: SchemaType
            allowed: tuple[int, ...] | tuple[str, ...] | list[
                tuple[eq_type, num_type]
            ] | re.Pattern[str] | None = None
            unit: str = ""
            used: bool = True
            nullable: bool = False
            fill: DataType | None = None
            description: str = ""
            post_apply: Callable[[SchemaType], DataType] = lambda x: cast(DataType, x)
