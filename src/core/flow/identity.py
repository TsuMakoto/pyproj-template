from src.core.flow import I


class Loader(I.Loader):
    def load(self, ipt):
        return ipt


class Processor(I.Processor):
    def run(self, ipt):
        return ipt


class Model(I.Model):
    def __call__(self, ipt):
        return ipt


class Evaluator(I.Evaluator):
    def evaluate(self, _: I.Model, ipt):
        return ipt


class Handler(I.Handler):
    def handle(self, ipt):
        return ipt


class Cross(I.Cross):
    def to_loader_input(self, ipt):
        return ipt

    def to_data_processor_input(self, out):
        return out

    def to_model_input(self, out):
        return out

    def to_model_processor_input(self, out):
        return out

    def to_evaluator_input(self, out):
        return out
