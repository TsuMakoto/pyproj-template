import enum
from enum import auto
from pathlib import Path
from typing import Callable


class Enum(enum.Enum):
    @property
    def lower(self):
        return self.name.lower()

    @classmethod
    def from_name(cls, name: str):
        return cls[name.upper()]


class enums:
    class System:
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

    class DateUtils:
        class Season(Enum):
            SPRING = "春"
            SUMMER = "夏"
            AUTUMN = "秋"
            WINTER = "冬"

        class Month(Enum):
            JAN = ("1月", "January", range(1, 32))
            FEB = ("2月", "February", range(1, 29))
            MAR = ("3月", "March", range(1, 32))
            APR = ("4月", "April", range(1, 31))
            MAY = ("5月", "May", range(1, 32))
            JUN = ("6月", "June", range(1, 31))
            JUL = ("7月", "July", range(1, 32))
            AUG = ("8月", "August", range(1, 32))
            SEP = ("9月", "September", range(1, 31))
            OCT = ("10月", "October", range(1, 32))
            NOV = ("11月", "November", range(1, 31))
            DEC = ("12月", "December", range(1, 32))

            def __init__(self, ja: str, en: str, days: range):
                self.ja = ja
                self.en = en
                self.days = days

                self.val = int(self.ja[0:-1])

        class Week(Enum):
            MON = ("Monday", "月", "月曜日")
            TUE = ("Tuesday", "火", "火曜日")
            WED = ("Wednesday", "水", "水曜日")
            THU = ("Thursday", "木", "木曜日")
            FRI = ("Friday", "金", "金曜日")
            SAT = ("Saturday", "土", "土曜日")
            SUN = ("Sunday", "日", "日曜日")

            def __init__(self, en: str, short_ja: str, ja: str):
                self.en = en
                self.short_ja = short_ja
                self.ja = ja

    class UserInfo:
        class Agent(Enum):
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

        class Sex(Enum):
            MAN = "男"
            WOMAN = "女"

        class Post(Enum):
            PRESIDENT = auto()
            VICE_PRESIDENT = auto()
            MANAGER = auto()
            STAFF = auto()

    class Colors:
        class base(Enum):
            def __init__(self, hex: str, r: int, g: int, b: int):
                self.hex = hex
                self.r = r
                self.g = g
                self.b = b

        class Main(base):
            RED = ("#F56C6C", 245, 108, 108)
            GREEN = ("67C23A", 103, 194, 58)
            BLUE = ("#409EFF", 64, 158, 255)
            YELLOW = ("#E6A23C", 230, 162, 60)
            GRAY = ("#909399", 144, 147, 153)

    class Extensions:
        class base(Enum):
            @property
            def ext(self) -> str:
                return self.value[1:]

            def __radd__(self, filename: str):
                return filename + self.value

        class Data(base):
            EXCEL = ".xlsx"
            CSV = ".csv"
            JSON = ".json"
            TXT = ".txt"

        class Image(base):
            PNG = ".png"
            JPG = ".jpg"
            JPEG = ".jpeg"
            GIF = ".gif"

        class Wav(base):
            WAV = ".wav"
            MP3 = ".mp3"
            OGG = ".ogg"

        class Text(base):
            TXT = ".txt"
            YML = ".yml"
            YAML = ".yaml"
            JSON = ".json"
            XML = ".xml"

        class Binary(base):
            BIN = ".bin"
            DAT = ".dat"
            PTH = ".pth"
            PKL = ".pkl"
            PDF = ".pdf"

    class FileUtils:
        class Encoding:
            UTF8 = "utf-8"
            SHIFT_JIS = "shift-jis"
            CP932 = "cp932"

        class Delimiter:
            COMMA = ","
            TAB = "\t"
            SPACE = " "

        class LineFeed:
            LF = "\n"
            CRLF = "\r\n"

    class Format:
        class Date(Enum):
            JA = "%Y年%m月%d日"
            SLASH = "%Y/%m/%d"
            HYPHEN = "%Y-%m-%d"
            DOT = "%Y.%m.%d"

        class Time(Enum):
            JA = "%H時%M分%S秒"
            COLON = "%H:%M:%S"

        class DateTime(Enum):
            JA = "%Y年%m月%d日 %H時%M分%S秒"
            SLASH = "%Y/%m/%d %H:%M:%S"
            HYPHEN = "%Y-%m-%d %H:%M:%S"
            DOT = "%Y.%m.%d %H:%M:%S"

    class Regex(Enum):
        PHONE_NUMBER = r"^(0\d{1,4}-\d{1,4}-\d{4})$"
        POSTAL_CODE = r"^\d{3}-\d{4}$"
        EMAIL = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    class DataUtils:
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

    class Dataset(Enum):
        MNIST = auto()
        CIFAR10 = auto()
        CIFAR100 = auto()
        IMAGENET = auto()
        CUSTOM = auto()

    class Model:
        class Mode(Enum):
            TRAIN = auto()
            TEST = auto()
            EVAL = auto()
            FIT = auto()
            PREDICT = auto()
            FIT_PREDICT = auto()
            SOLVE = auto()
            TRANSFORM = auto()

        class Define(Enum):
            INIT = auto()
            LOAD = auto()

        class Variable(Enum):
            class Type:
                INTEGER = "int"
                FLOAT = "float"
                BINARY = "binary"

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

        class Classification:
            class Classical:
                class Algorithm(Enum):
                    KMEANS = auto()
                    KMEANSpp = auto()
                    DBSCAN = auto()

                class Distance(Enum):
                    EUCLIDEAN = auto()
                    DTW = auto()

        class Net:
            class Mode(Enum):
                TRAIN = auto()
                TEST = auto()
                EVAL = auto()

            class Layer(Enum):
                LINEAR = auto()
                CONVOLUTION = auto()
                MAX_POOLING = auto()
                AVERAGE_POOLING = auto()
                BATCH_NORMALIZATION = auto()
                DROPOUT = auto()
                ACTIVATION = auto()

            class Activation(Enum):
                RELU = auto()
                SIGMOID = auto()
                TANH = auto()
                SOFTMAX = auto()

            class Loss(Enum):
                MSE = auto()
                BCE = auto()
                CE = auto()

            class Optimizer(Enum):
                SGD = auto()
                ADAM = auto()

            class Scheduler(Enum):
                STEP = auto()
                MULTI_STEP = auto()
                COSINE = auto()

            class Metric(Enum):
                ACCURACY = auto()
                PRECISION = auto()
                RECALL = auto()
                F1 = auto()

        class Optimal:
            class Mode(Enum):
                MIN = auto()
                MAX = auto()

            class Solver(Enum):
                SCIPY = auto()
                SCIP = auto()
                CBC = auto()
                CPLEX = auto()
                GUROBI = auto()

            class Constraint(Enum):
                LE = auto()
                GE = auto()
                EQ = auto()

    class AWS:
        class S3:
            class Minio(Enum):
                ACCESS_KEY = "minioadmin"
                SECRET_KEY = "minioadmin"
                ENDPOINT = "localhost:9000"
                REGEON = "us-east-1"

    class Path(Enum):
        DATASETS = Path("./datasets")
        PRIVATE_DATASETS = Path("./datasets/private")
        PUBLIC_DATASETS = Path("./datasets/public")
        GALLERY = Path("./gallery")
        LIBS = Path("./libs")
        MODELS = Path("./models")
        NOTEBOOKS = Path("./notebooks")
        REPORTS = Path("./reports")
        SRC = Path("./src")
        LOGS = Path("./logs")
        RESULTS = Path("./results")
        CONFIGS = Path("./configs")
        TESTS = Path("./tests")
        DOCS = Path("./docs")
        TOOLS = Path("./tools")
        TMP = Path("./tmp")

        def __truediv__(self, other: Path | str):
            return self.value / other
