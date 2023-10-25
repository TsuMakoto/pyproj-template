def free(ipt_struct):
    """
    デバッグ用
    全体構成として、input,outputととして、
    NamedTupleのimmutableで入出力を決定しているため、
    console上で利用する場合、構造体をimportする必要があり、そのままつかえない。
    不便なので、args,kwargsでも入力可能にしている。

    例えば、
    class Input(NamedTuple)
    def func(this, ipt: Input)があったときに、
    > import func, Input
    > func.func(Input(1,2,3))
    とする必要があるが、
    > import func
    > func.func(1,2,3)
    とすることができる。

    ただし、mypy上エラーとなるので本当にデバッグ用。
    """
    def _wrapper(func):
        def wrapper(*args, **kwargs):
            this = args[0]
            ipt = args[1:]
            if len(ipt) == 1 and isinstance(ipt[0], ipt_struct):
                ipt = ipt[0]
            return func(this, ipt_struct(*ipt, **kwargs))
        return wrapper
    return _wrapper
