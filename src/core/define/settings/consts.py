import sys
from pathlib import Path
from typing import Final, Generic, TypeVar

T = TypeVar('T')


class _Const:
    class Define(Generic[T]):
        def __init__(self, id_: int, val: T, **kwargs):
            self.id = id_
            self.val = val
            for k, v in kwargs.items():
                setattr(self, k, v)

        def __eq__(self, other):
            return self.id == other.id and self.val == other.val

        def __hash__(self):
            return hash((self.id, self.val))

        @property
        def get(self) -> Final[T]:
            return self.val

    def __init__(self):
        self.id = 0

    def __call__(self, val: T, **kwargs) -> "_Const.Define[T]":
        self.id += 1
        return _Const.Define(self.id, val, **kwargs)


class _Consts:
    define = _Const()


class consts(_Consts):
    # --------------------------------------------------
    # 汎用
    # --------------------------------------------------

    class Regex:
        PHONE_NUMBER = _Consts.define(r"0\d{1,4}-\d{1,4}-\d{4}")
        POSTAL_CODE = _Consts.define(r"\d{3}-\d{4}")
        EMAIL = _Consts.define(
            r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

    class Format:
        DATE = _Consts.define(
            "%Y-%m-%d",
            ja="%Y年%m月%d日",
            slash="%Y/%m/%d",
            hyphen="%Y-%m-%d",
            dot="%Y.%m.%d",
        )
        DATETIME = _Consts.define(
            "%Y-%m-%d %H:%M:%S",
            ja="%Y年%m月%d日 %H時%M分%S秒",
            slash="%Y/%m/%d %H:%M:%S",
            hyphen="%Y-%m-%d %H:%M:%S",
            dot="%Y.%m.%d %H:%M:%S"
        )
        TIME = _Consts.define(
            "%H:%M:%S",
            ja="%H時%M分%S秒"
        )

    class Month:
        JAN = _Consts.define("January", ja="1月")
        FEB = _Consts.define("February", ja="2月")
        MAR = _Consts.define("March", ja="3月")
        APR = _Consts.define("April", ja="4月")
        MAY = _Consts.define("May", ja="5月")
        JUN = _Consts.define("June", ja="6月")
        JUL = _Consts.define("July", ja="7月")
        AUG = _Consts.define("August", ja="8月")
        SEP = _Consts.define("September", ja="9月")
        OCT = _Consts.define("October", ja="10月")
        NOV = _Consts.define("November", ja="11月")
        DEC = _Consts.define("December", ja="12月")

    class Week:
        MON = _Consts.define("Monday", ja="月曜日")
        TUE = _Consts.define("Tuesday", ja="火曜日")
        WED = _Consts.define("Wednesday", ja="水曜日")
        THU = _Consts.define("Thursday", ja="木曜日")
        FRI = _Consts.define("Friday", ja="金曜日")
        SAT = _Consts.define("Saturday", ja="土曜日")
        SUN = _Consts.define("Sunday", ja="日曜日")

    class Season:
        SPRING = _Consts.define("Spring", ja="春")
        SUMMER = _Consts.define("Summer", ja="夏")
        AUTUMN = _Consts.define("Autumn", ja="秋")
        WINTER = _Consts.define("Winter", ja="冬")

    class Status:
        OK = _Consts.define("OK")
        ERROR = _Consts.define("ERROR")
        WARNING = _Consts.define("WARNING")

    class Extension:
        EXCEL = _Consts.define("xlsx")
        CSV = _Consts.define("csv")
        JSON = _Consts.define("json")
        YAML = _Consts.define("yaml")
        YML = _Consts.define("yml")
        TXT = _Consts.define("txt")
        XML = _Consts.define("xml")
        PDF = _Consts.define("pdf")
        PNG = _Consts.define("png")
        JPG = _Consts.define("jpg")
        GIF = _Consts.define("gif")
        MP4 = _Consts.define("mp4")
        WAV = _Consts.define("wav")
        ZIP = _Consts.define("zip")
        DAT = _Consts.define("dat")
        DAT = _Consts.define("dat")
        PKL = _Consts.define("pkl")
        PTH = _Consts.define("pth")

    class Encoding:
        UTF8 = _Consts.define("utf-8")
        UTF16 = _Consts.define("utf-16")
        SHIFT_JIS = _Consts.define("shift-jis")
        EUC_JP = _Consts.define("euc-jp")

    class Delimiter:
        COMMA = _Consts.define(",")
        TAB = _Consts.define("\t")
        SPACE = _Consts.define(" ")

    class LineFeed:
        CRLF = _Consts.define("\r\n")
        LF = _Consts.define("\n")

    class OS:
        WINDOWS = _Consts.define("windows")
        MAC = _Consts.define("mac")
        LINUX = _Consts.define("linux")

    class MAX:
        INT = _Consts.define(sys.maxsize)
        FLOAT = _Consts.define(sys.float_info.max)

    # --------------------------------------------------
    # 学習モデル関連
    # --------------------------------------------------

    class Optimizer:
        SGD = _Consts.define("SGD")
        ADAM = _Consts.define("Adam")
        ADAGRAD = _Consts.define("Adagrad")
        ADADELTA = _Consts.define("Adadelta")
        RMS_PROP = _Consts.define("RMSprop")

    class Loss:
        MSE = _Consts.define("MSE")
        MAE = _Consts.define("MAE")
        RMSE = _Consts.define("RMSE")
        R2 = _Consts.define("R2")

    class Metric:
        ACCURACY = _Consts.define("accuracy")
        PRECISION = _Consts.define("precision")
        RECALL = _Consts.define("recall")
        F1 = _Consts.define("f1")

    class Layer:
        DENSE = _Consts.define("Dense")
        CONV2D = _Consts.define("Conv2D")
        MAX_POOLING2D = _Consts.define("MaxPooling2D")
        FLATTEN = _Consts.define("Flatten")
        LSTM = _Consts.define("LSTM")
        GRU = _Consts.define("GRU")
        BIDIRECTIONAL = _Consts.define("Bidirectional")
        DROPOUT = _Consts.define("Dropout")
        BATCH_NORMALIZATION = _Consts.define("BatchNormalization")

    class Activation:
        RELU = _Consts.define("relu")
        SIGMOID = _Consts.define("sigmoid")
        SOFTMAX = _Consts.define("softmax")
        TANH = _Consts.define("tanh")
        LINEAR = _Consts.define("linear")

    class Padding:
        SAME = _Consts.define("same")
        VALID = _Consts.define("valid")

    class Pooling:
        MAX = _Consts.define("max")
        AVG = _Consts.define("avg")

    # --------------------------------------------------
    # ファイルパス
    # --------------------------------------------------
    class PathName:
        PARENT = _Consts.define("..")
        DATASET = _Consts.define("dataset")
        REPORTS = _Consts.define("reports")
        MODELS = _Consts.define("models")
        LOGS = _Consts.define("logs")
        KEYS = _Consts.define("keys")

        for p in [DATASET, REPORTS, MODELS]:
            p.path = Path(p.get)

    # --------------------------------------------------
    # AWS
    # --------------------------------------------------
    class AWS:
        class S3:
            class Minio:
                ACCESS_KEY = _Consts.define("minioadmin")
                SECRET_KEY = _Consts.define("minioadmin")
                ENDPOINT = _Consts.define("localhost:9000")
                REGEON = _Consts.define("us-east-1")


__all__ = ['consts']
