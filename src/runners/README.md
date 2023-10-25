### Runner

以下に例

```python
from typing import NamedTuple

import matplotlib.pyplot as plt
from src import factory
from src.runners.base import Runner as BaseRunner


# 汎用化のため、パイプライン全体に必要なパラメータがあれば設定
class Params(NamedTuple):
    dataname: str
    layer_num: int
    epoch: int
    # ...etc


# Handlerをつかわない場合など、基本てきには以下
class Runner(BaseRunner):
    def __init__(self, **kwargs):
        self.params = Params(**kwargs)

    def initialize(self):
        self.loader = factory.Loader.create()
        self.data_processor = factory.DataProcessor.create()
        self.model = factory.Model.predict_model()
        self.evaluator = factory.Evaluator.create()

    def _run(self):
        # load
        ipt = factory.Loader.Input()
        data = self.loader.load(ipt)

        # dataをdata_processorの入力へ変換
        out = ...

        # process
        ipt = factory.DataProcessor.Input(out)
        preprocessed = self.loader.load(ipt)

        # preprocessedをmodelの入力へ変換
        out = ...

        # modeling
        ipt = factory.Model.Input(out)
        result self.model(ipt)

        # modelの出力を評価の入力へ変換
        out = ...

        ipt = factory.Evaluator.Input(out)
        evaluated = self.evaluator.evaluate(ipt)

        # 例えば可視化など
        ...
        plt.show()
```
