from enum import Enum, auto
from typing import Callable


class _Enum(Enum):
    def lower(self):
        return self.name.lower()

    def from_name(name: str):
        return _Enum.base[name.upper()]


class enums:
    base = _Enum

    # --------------------------------------------------
    # 開発関連
    # --------------------------------------------------
    class LogLevel(base):
        DEBUG = auto()
        INFO = auto()
        WARNING = auto()
        ERROR = auto()
        CRITICAL = auto()

    class Status(base):
        OK = auto()
        ERROR = auto()
        WARNING = auto()

    # --------------------------------------------------
    # 汎用
    # --------------------------------------------------
    class Week(base):
        MON = ("Monday", "月", "月曜日")
        TUE = ("Tuesday", "火", "火曜日")
        WED = ("Wednesday", "水", "水曜日")
        THU = ("Thursday", "木", "木曜日")
        FRI = ("Friday", "金", "金曜日")
        SAT = ("Saturday", "土", "土曜日")
        SUN = ("Sunday", "日", "日曜日")

        def __init__(self, *names):
            self.en_name = names[0]
            self.short_jp_name = names[1]
            self.jp_name = names[2]

    class Season(base):
        SPRING = "春"
        SUMMER = "夏"
        AUTUMN = "秋"
        WINTER = "冬"

    class Month(base):
        JAN = ("1月", "January")
        FEB = ("2月", "February")
        MAR = ("3月", "March")
        APR = ("4月", "April")
        MAY = ("5月", "May")
        JUN = ("6月", "June")
        JUL = ("7月", "July")
        AUG = ("8月", "August")
        SEP = ("9月", "September")
        OCT = ("10月", "October")
        NOV = ("11月", "November")
        DEC = ("12月", "December")

        def __init__(self, *names):
            self.jp_name = names[0]
            self.en_name = names[1]

            self.val = int(self.jp_name[0:-1])

    class Switch(base):
        ON = auto()
        OFF = auto()

    class Color(base):
        RED = auto()
        GREEN = auto()
        BLUE = auto()

    class Sex(base):
        MAN = "男"
        WOMAN = "女"

    class Post(base):
        PRESIDENT = auto()
        VICE_PRESIDENT = auto()
        MANAGER = auto()
        STAFF = auto()

    class UserAgent(base):
        CHROME = auto()
        FIREFOX = auto()
        SAFARI = auto()
        IE = auto()
        EDGE = auto()
        OPERA = auto()

    class OS(base):
        WINDOWS = auto()
        MAC = auto()
        LINUX = auto()

    class DataExtension(base):
        EXCEL = (auto(), ".xlsx")
        CSV = (auto(), ".csv")
        JSON = (auto(), ".json")
        TXT = (auto(), ".txt")

    class ImageExtension(base):
        PNG = (auto(), ".png")
        JPG = (auto(), ".jpg")
        JPEG = (auto(), ".jpeg")
        GIF = (auto(), ".gif")

    class WavExtension(base):
        WAV = (auto(), ".wav")
        MP3 = (auto(), ".mp3")
        OGG = (auto(), ".ogg")

    class TextExtension(base):
        TXT = (auto(), ".txt")
        YML = (auto(), ".yml")
        YAML = (auto(), ".yaml")
        JSON = (auto(), ".json")
        XML = (auto(), ".xml")

    class BinaryExtension(base):
        BIN = (auto(), ".bin")
        DAT = (auto(), ".dat")
        PTH = (auto(), ".pth")

    # --------------------------------------------------
    # データ関連
    # --------------------------------------------------

    class Empty(base):
        NONE = (auto(), None)
        STR = (auto(), "")
        LIST = (auto(), [])
        DICT = (auto(), {})
        SET = (auto(), set())
        TUPLE = (auto(), ())

        def __init__(self, id_, val):
            self.id = id_
            self.val = val

        def __call__(self):
            return self.val

        @classmethod
        def check(cls, val):
            return any([val == e.val for e in cls])

    # --------------------------------------------------
    # 学習モデル関連
    # --------------------------------------------------
    class Mode(_Enum):
        TRAIN = auto()
        TEST = auto()
        EVAL = auto()

    class Device(base):
        CPU = "cuda"
        GPU = "cpu"

        @classmethod
        def use(cls,
                gpu_availablility: Callable[[], bool],
                gpu_name: str = "",
                gpu_number: int = 0) -> str:

            if not gpu_availablility():
                return cls.CPU.value

            if gpu_name == "":
                gpu_name = cls.GPU.value

            return f"{gpu_name}:{gpu_number}"

    # --------------------------------------------------
    # 数理最適化関連
    # --------------------------------------------------
    class OptimSolver(base):
        SCIPY = auto()
        SCIP = auto()
        CBC = auto()
        CPLEX = auto()
        GUROBI = auto()

    class OptimSense(base):
        MINIMIZE = auto()
        MAXIMIZE = auto()

    class OptimStatus(base):
        OPTIMAL = auto()
        INFEASIBLE = auto()
        UNBOUNDED = auto()
        INFEASIBLE_OR_UNBOUNDED = auto()
        ERROR = auto()
        NOT_SOLVED = auto()

    class OptimResult(base):
        SUCCESS = auto()
        FAILURE = auto()

    class OptimConstraint(base):
        LE = auto()
        GE = auto()
        EQ = auto()


__all__ = ['enums']
