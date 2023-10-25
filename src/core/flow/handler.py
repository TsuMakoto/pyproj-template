from typing import TypeVar

from src.core.flow import I, identity

_I = TypeVar('_I', contravariant=True)
_O = TypeVar('_O', covariant=True)


class Handler(I.Handler[_I, _O]):
    __cross: I.Cross = identity.Cross()
    __loader: I.Loader = identity.Loader()
    __data_processor: I.Processor = identity.Processor()
    __model: I.Model = identity.Model()
    __evaluator: I.Evaluator = identity.Evaluator()

    def __init__(self,
                 input_is_data: bool = False,
                 is_eval_model: bool = True):
        self.input_is_data = input_is_data
        self.is_eval_model = is_eval_model

    def handle(self, ipt):
        out = ipt

        if not self.input_is_data:
            ipt = self.__cross.to_loader_input(out)
            out = self.__loader.load(ipt)

            ipt = self.__cross.to_data_processor_input(out)
            out = self.__data_processor.run(ipt)

        ipt = self.__cross.to_model_input(out)
        out = self.__model(ipt)

        if self.is_eval_model:
            ipt = self.__cross.to_evaluator_input(out)
            out = self.__evaluator.evaluate(self.__model, ipt)

        return out

    def set_cross(self, cross: I.Cross):
        self.__cross = cross

    def set_loader(self, loader: I.Loader):
        self.__loader = loader

    def set_data_processor(self, data_processor: I.Processor):
        self.__data_processor = data_processor

    def set_model(self, model: I.Model):
        self.__model = model

    def set_evaluator(self, evaluator: I.Evaluator):
        self.__evaluator = evaluator
