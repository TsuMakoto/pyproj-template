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


class Optimizater(Model, Generic[I_, O_]):
    ...


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
IOptimizater = Optimizater
INet = Net
ITrainer = Trainer
IEvaluator = Evaluator
IProcessor = Processor
IAPICaller = APICaller
