import json
from pathlib import Path

from src.core.helper import logger
from src.core.utils.validate_dict import ValidateDict


@logger.execution_time
def parse(filepath: str | Path):
    with open(filepath, "r") as f:
        d = json.load(f)

    # Validation
    validator = ValidateDict(**d)
    with validator:  # as vd:
        # vd.validate("name", str)
        ...

    return d
