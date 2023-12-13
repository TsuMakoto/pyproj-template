from interfaces import Model as IModel

from .custom import typing
from .interfaces import Evaluator as IEvaluator
from .interfaces import Loader as ILoder
from .interfaces import Processor as IProcessor

__all__ = ["typing", "IModel", "IEvaluator", "ILoder", "IProcessor"]
