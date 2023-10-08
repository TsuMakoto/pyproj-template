import enum
from enum import auto
from typing import Callable


class Enum(enum.Enum):
    def lower(self):
        return self.name.lower()

    @classmethod
    def from_name(cls, name: str):
        return cls[name.upper()]


class Enums:
    # --------------------------------------------------
    # 開発関連
    # --------------------------------------------------
    class LogLevel(Enum):
        DEBUG = auto()
        INFO = auto()
        WARNING = auto()
        ERROR = auto()
        CRITICAL = auto()

    class Status(Enum):
        OK = auto()
        ERROR = auto()
        WARNING = auto()

    # --------------------------------------------------
    # 汎用
    # --------------------------------------------------
    class Week(Enum):
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

    class Season(Enum):
        SPRING = "春"
        SUMMER = "夏"
        AUTUMN = "秋"
        WINTER = "冬"

    class Month(Enum):
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

    class Switch(Enum):
        ON = auto()
        OFF = auto()

    class RGB(Enum):
        RED = auto()
        GREEN = auto()
        BLUE = auto()

    class Sex(Enum):
        MAN = "男"
        WOMAN = "女"

    class Post(Enum):
        PRESIDENT = auto()
        VICE_PRESIDENT = auto()
        MANAGER = auto()
        STAFF = auto()

    class UserAgent(Enum):
        CHROME = auto()
        FIREFOX = auto()
        SAFARI = auto()
        IE = auto()
        EDGE = auto()
        OPERA = auto()

    class OS(Enum):
        WINDOWS = auto()
        MAC = auto()
        LINUX = auto()

    class DataExtension(Enum):
        EXCEL = (auto(), ".xlsx")
        CSV = (auto(), ".csv")
        JSON = (auto(), ".json")
        TXT = (auto(), ".txt")

    class ImageExtension(Enum):
        PNG = (auto(), ".png")
        JPG = (auto(), ".jpg")
        JPEG = (auto(), ".jpeg")
        GIF = (auto(), ".gif")

    class WavExtension(Enum):
        WAV = (auto(), ".wav")
        MP3 = (auto(), ".mp3")
        OGG = (auto(), ".ogg")

    class TextExtension(Enum):
        TXT = (auto(), ".txt")
        YML = (auto(), ".yml")
        YAML = (auto(), ".yaml")
        JSON = (auto(), ".json")
        XML = (auto(), ".xml")

    class BinaryExtension(Enum):
        BIN = (auto(), ".bin")
        DAT = (auto(), ".dat")
        PTH = (auto(), ".pth")

    # --------------------------------------------------
    # データ関連
    # --------------------------------------------------

    class Empty(Enum):
        NONE = auto()
        STR = auto()
        LIST = auto()
        DICT = auto()
        SET = auto()
        TUPLE = auto()

        def __call__(self):
            return {
                self.NONE: None,
                self.STR: "",
                self.LIST: [],
                self.DICT: {},
                self.SET: set(),
                self.TUPLE: tuple()
            }[self]

        @classmethod
        def check(cls, val):
            return any([val == e() for e in cls])

    # --------------------------------------------------
    # 学習モデル関連
    # --------------------------------------------------
    class Mode(Enum):
        TRAIN = auto()
        TEST = auto()
        EVAL = auto()

    class Device(Enum):
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
    class OptimSolver(Enum):
        SCIPY = auto()
        SCIP = auto()
        CBC = auto()
        CPLEX = auto()
        GUROBI = auto()

    class OptimSense(Enum):
        MINIMIZE = auto()
        MAXIMIZE = auto()

    class OptimStatus(Enum):
        OPTIMAL = auto()
        INFEASIBLE = auto()
        UNBOUNDED = auto()
        INFEASIBLE_OR_UNBOUNDED = auto()
        ERROR = auto()
        NOT_SOLVED = auto()

    class OptimResult(Enum):
        SUCCESS = auto()
        FAILURE = auto()

    class OptimConstraint(Enum):
        LE = auto()
        GE = auto()
        EQ = auto()


__all__ = ['Enum', 'Enums']
