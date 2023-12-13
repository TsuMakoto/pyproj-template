### Processor

以下に例

```python
from typing import NamedTuple

from src.core.structs import IProcessor

from src.core.helper import logger

class struct:
  class Params(NamedTuple):
    ...

  class Input(NamedTuple):
    ...

  class Output(NamedTuple):
    ...

class types:
  Processor = IProcessor[struct.Input, struct.Output]



class Processor(types.Processor):
    def __init__(self, params: struct.Params):
      ...

    @logger.execution_time
    def run(self, ipt: struct.Input) -> struct.Output:
      return struct.Output()
```
