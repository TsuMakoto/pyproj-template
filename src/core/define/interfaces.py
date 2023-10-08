from typing import Generic, Protocol, TypeVar

I_ = TypeVar('I_')
O_ = TypeVar('O_')


class Handler(Protocol, Generic[I_, O_]):
    def __init__(self, params):
        ...

    def handle(self, input_: I_) -> O_:
        ...


class DataLoader(Protocol, Generic[I_, O_]):
    def __init__(self, params):
        ...

    def load(self, input_: I_) -> O_:
        ...


class Model(Protocol, Generic[I_, O_]):
    def __init__(self, params):
        ...

    def __call__(self, input_: I_) -> O_:
        ...

# --------------------------------------------
# 数理最適化のためのインターフェース
# --------------------------------------------


class OptimModel(Model, Generic[I_, O_]):
    ...


class OptimProblem(Protocol, Generic[I_, O_]):
    def __init__(self, params):
        ...

    def make(self, input_: I_) -> O_:
        ...


class Constraint(Protocol, Generic[I_, O_]):
    def __init__(self, params):
        ...

    def __call__(self, input_: I_) -> O_:
        ...


class Objective(Protocol, Generic[I_, O_]):
    def __init__(self, params):
        ...

    def __call__(self, input_: I_) -> O_:
        ...


class Solver(Protocol, Generic[I_, O_]):
    def __init__(self, params):
        ...

    def solve(self, input_: I_) -> O_:
        ...


# --------------------------------------------
# 機械学習のためのインターフェース
# --------------------------------------------

class Net(Model, Generic[I_, O_]):
    def forward(self, input_: I_) -> O_:
        ...

    def backward(self, input_: I_) -> O_:
        ...


class Trainer(Protocol, Generic[I_, O_]):
    def __init__(self, params):
        ...

    def train(self, input_: I_) -> O_:
        ...


class Evaluator(Protocol, Generic[I_, O_]):
    def __init__(self, params):
        ...

    def evaluate(self, input_: I_) -> O_:
        ...


class Processor(Protocol, Generic[I_, O_]):
    def __init__(self, params):
        ...

    def run(self, input_: I_) -> O_:
        ...


class APICaller(Protocol, Generic[I_, O_]):
    def response(self, input_: I_) -> O_:
        ...


IHandler = Handler
IDataLoader = DataLoader
IModel = Model
IOptimModel = OptimModel
IOptimProblem = OptimProblem
IConstraint = Constraint
IObjective = Objective
ISolver = Solver
INet = Net
ITrainer = Trainer
IEvaluator = Evaluator
IProcessor = Processor
IAPICaller = APICaller
