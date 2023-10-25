### Loader

以下に例

```python
from pathlib import Path
from typing import NamedTuple

import numpy as np
import pandas as pd
from src.core.flow import I
from src.core.helper.decorators.tuple_to import free
from src.core.settings.enums import enums


class struct:
    class Params(NamedTuple):
        delimiter: str = enums.FileUtils.Delimiter.COMMA
        dataroot: Path = enums.Path.PRIVATE_DATASETS

    class Input(NamedTuple):
        dataname: Path | str

    class Output(pd.DataFrame):
        id: "pd.Series[int]"
        name: "pd.Series[str]"
        address: "pd.Series[str]"

class DataLoader(I.Loader):
    @free(struct.Params)
    def __init__(self, params: struct.Params):
        self.params = params

    @free(struct.Input)
    def load(self, ipt: struct.Input) -> struct.Output:
        ext = enums.Extensions.Text.TXT
        delimiter = self.params.delimiter

        data = np.loadtxt(self.params.dataroot / (ipt.dataname + ext)

        df = pd.DataFrame(data=data, columns=["id", "name", "address"])

        return df
```

```shell
$ params = struct.Params()
$ ipt = struct.Input("user")
$ DataLoader(params).load(ipt)

# or

$ DataLoader().load("user") # ただし、型エラー
```
