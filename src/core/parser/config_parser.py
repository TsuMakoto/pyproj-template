from pathlib import Path

import yaml
from src.core.helper import logger
from src.core.parser.constructors import constructors
from src.core.utils.validate_dict import ValidateDict


@logger.execution_time
def parse(filepath: str | Path, levels: list[str] = []):
    loader = yaml.SafeLoader

    for tag, constructor in constructors.items():
        loader.add_constructor(tag, constructor)

    with open(filepath, "r") as f:
        d = yaml.load(f, Loader=loader)

    for level in levels:
        d = d[level]

    # Validation
    validator = ValidateDict(**d)
    with validator:  # as vd:
        # vd.validate("name", str)
        ...

    return d
