from pathlib import Path

import yaml


def __path_constructor(loader: yaml.SafeLoader, node: yaml.nodes.ScalarNode):
    return Path(str(loader.construct_scalar(node)))


constructors = {
    "!path": __path_constructor,
}
