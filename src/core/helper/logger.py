import inspect
import sys

from loguru import logger
from src.core.settings import enums

logger.remove()

for log_level in enums.System.LogLevel:
    logger.level(log_level.name, color=f"<{log_level.color}>")

fmt = ""
fmt += "<bold><level>{level: <8}</level></bold>"
fmt += " | "
fmt += "<white>{time:YYYY-MM-DD HH:mm:ss}</white>"
fmt += " | "
fmt += "<cyan>{elapsed}</cyan>"
fmt += " | "
fmt += "<bold>{message}</bold>"

logger.add(sys.stdout, format=fmt, colorize=True)
logger.add("./logs/loguru/{time}.log", rotation="1days")


def execution_time(func):
    def wrapper(*args, **kwargs):
        class_name = func.__qualname__
        if "." in class_name:
            class_name = ".".join(func.__qualname__.split(".")[:-1])

        func_name = func.__name__

        filepath = inspect.getfile(func).split("src")[1]
        filepath = "src" + ".".join(filepath.split("/"))[:-3]

        logger.info(f"Called function: {filepath}->{class_name}->{func_name}")

        result = func(*args, **kwargs)

        return result

    return wrapper


class LoggerWriter:
    """
    標準出力とログ出力を同時に行うためのクラス
    """

    def __init__(self, level):
        self.level = level

    def write(self, message):
        # 末尾の改行を削除してログ出力
        if message != "\n":
            self.level(message.strip())

    def flush(self):
        self.level(sys.stderr)


debug = logger.debug
info = logger.info
warning = logger.warning
error = logger.error
critical = logger.critical
