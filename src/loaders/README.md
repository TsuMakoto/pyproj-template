### Loader

以下に例

```python
from typing import NamedTuple

from src.core.structs import ILoader

from src.core.helper import logger

class struct:
  class Params(NamedTuple):
    ...

  class Input(NamedTuple):
    ...

  class Output(NamedTuple):
    ...

class types:
  Loader = ILoader[struct.Input, struct.Output]


class DataLoader(types.Loader):
    def __init__(self, params: struct.Params):
        self.params = params

    @logger.execution_time
    def load(self, ipt: struct.Input) -> struct.Output:
        return struct.Output()
```

