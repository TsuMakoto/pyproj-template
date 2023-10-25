### Model

以下に例

```python
from pathlib import Path
from typing import NamedTuple
import numpy as np
from numpy.typing import NDArray

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

from src.core.flow import I
from src.core.helper.decorators.tuple_to import free



class struct:
    class NetParams(NamedTuple):
        layer_num: int = 500
        device: str = "cpu"

    class Model:
        class Input(NamedTuple):
            x: NDArray[np.float64]

        class Params(NamedTuple):
            net_params: "struct.NetParams"

        class Output(pd.DataFrame):
            label: x: NDArray[np.float64]

    class Train:
        class Input(NamedTuple):
            train_loader: torch.utils.data.DataLoader

        class Params(NamedTuple):
            net_params: "struct.NetParams"
            epoch: int

class Net(nn.Module):
    def __init__(self, params: struct.NetParams):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(28 * 28, params.layer_num)
        self.fc2 = nn.Linear(layer_num, 10)

    def forward(self, x):
        x = x.view(-1, 28 * 28)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

class Model(I.Model):
    @free(struct.Model.Params)
    def __init__(self, params: struct.Model.Params):
        net_params = struct.NetPrams(*params.net_params)
        self.net = Net(net_params).to(params.device)

    @free(struct.Input)
    def __call__(self, ipt: struct.Input) -> struct.Model.Output:
        return self.net(ipt.x)


class Train(I.Model):
    @free(struct.Model.Params)
    def __init__(self, params: struct.Train.Params):
        self.epoch = params.epoch
        self.net_params = struct.NetPrams(*params.net_params)
        self.net = Net(net_params).to(self.net_params.device)
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    @free(struct.Input)
    def __call__(self, ipt: struct.Input):
        # 学習のループ
        for epoch in range(self.epoch):
            running_loss = 0.0
            for i, data in enumerate(ipt.train_loader, 0):
                inputs, labels = data[0].to(device), data[1].to(self.net_params.device)
                self.optimizer.zero_grad()
                outputs = self.net(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()
                running_loss += loss.item()
        
            print(f"Epoch {epoch+1}, Loss: {running_loss / (i+1)}")
        
        print("Finished Training")


```
