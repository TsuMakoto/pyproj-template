from typing import Protocol, TypeVar

I_ = TypeVar('I_', contravariant=True)
O_ = TypeVar('O_', covariant=True)

# 処理フローとして
# 1. Handler で入力を受け取る
# 2. Loader で入力を読み込み、処理対象データ等を作成・取得
# 3+n. Processor でデータに対して任意の処理を行う
# n+3. 前処理されたデータをModelに渡す
# n+4. Model で処理を行う
# ... ModelをEvaluatorで評価=>出力


class Handler(Protocol[I_, O_]):
    def handle(self, ipt: I_) -> O_: ...


class Loader(Protocol[I_, O_]):
    def load(self, ipt: I_) -> O_: ...


class Processor(Protocol[I_, O_]):
    def run(self, ipt: I_) -> O_: ...


class Model(Protocol[I_, O_]):
    def __call__(self, ipt: I_) -> O_: ...


class Evaluator(Protocol[I_, O_]):
    def evaluate(self, model: Model, ipt: I_) -> O_: ...


class Cross(Protocol):
    def to_loader_input(self, output): ...
    def to_data_processor_input(self, output): ...
    def to_model_input(self, output): ...
    def to_evaluator_input(self, output): ...
