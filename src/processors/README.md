### Processor

以下に例

```python
from typing import NamedTuple

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from src.core.flow import I
from src.core.helper.decorators.tuple_to import free
from src.services import data_processing


class struct:
    class Params(NamedTuple):
        pass

    class Input(NamedTuple):
        df: pd.DataFrame

    class Output(NamedTuple):
        features: NDArray[np.float64]


class Processor(I.Processor):
    @free(struct.Params)
    def __init__(self, params: struct.Params):
        self.window_size = params.window_size

    @free(struct.Input)
    def run(self, ipt: struct.Input) -> struct.Output:
        df = ipt.df

        features = data_processing.standard_scaler(df)

        return struct.Output(features=features)
```
