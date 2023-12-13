from typing import Protocol, TypeVar

I_ = TypeVar("I_", contravariant=True)
O_ = TypeVar("O_", covariant=True)


class Loader(Protocol[I_, O_]):
    def load(self, ipt: I_) -> O_:
        ...


class Processor(Protocol[I_, O_]):
    def run(self, ipt: I_) -> O_:
        ...


# ----------------------------------------
# モデルのカプセル化を行う
# ----------------------------------------
