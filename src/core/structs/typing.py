import typing

# ----------------------------------------
# Raw dataやAPI json, 設定ファイルなどの型定義などしたい場合はここに
# ここは構造体のみ記載して、実装したい場合は、./implに記載する
# ----------------------------------------


class MyDataStruct(typing.NamedTuple):
    hoge: str
    fuga: int
    foo: list
