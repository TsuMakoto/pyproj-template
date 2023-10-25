### Factory

以下に例

```python

from src.processors.data_processor import DataProcessor, struct

class DataProcessor:
    Input = struct.Input

    class Creator(struct.Params):
        def create(self):
            return DataLoader(self)

    @staticmethod
    def create():
        return DataProcessor.Creator().create()

```
