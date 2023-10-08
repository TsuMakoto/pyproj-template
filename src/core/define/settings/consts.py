import sys
from pathlib import Path
from typing import Generic, NamedTuple, Protocol, TypeVar

T = TypeVar('T', covariant=True)
U = TypeVar('U')


class Const(Protocol[T]):
    """
    定数クラスのプロトコル。

    このプロトコルは、定数オブジェクトのインターフェースを示すものです。
    ジェネリック型変数 T を持つ任意のオブジェクトがこのインターフェースを満たすことが期待されます。

    Attributes:
        id_ (int): 定数のID。
        val (T): 定数の値。

    Methods:
        get: 定数の値を取得するためのプロパティ。
    """

    def __init__(self, id_: int, val: T) -> None:
        """
        Const クラスのコンストラクタ。

        Args:
            id_ (int): 定数のID。
            val (T): 定数の値。
        """
        ...

    @property
    def get(self) -> T:
        """
        定数の値を取得するためのプロパティ。

        Returns:
            T: 定数の値。
        """
        ...


class _Const(Const, Generic[U]):
    def __init__(self, id_: int, val: U):
        self.id = id_
        self.__val = val

    def __eq__(self, other):
        return self.id == other.id and self.__val == other.__val

    def __hash__(self):
        return hash((self.id, self.__val))

    @property
    def get(self) -> U:
        return self.__val


class _DefineConst:
    def __init__(self):
        self.id = 0

    def __call__(self, val: U) -> Const[U]:
        self.id += 1

        return _Const[U](self.id, val)


class Structs:
    class Format:
        class Date(NamedTuple):
            ja: Const[str]
            slash: Const[str]
            hyphen: Const[str]
            dot: Const[str]

    class Translate(NamedTuple):
        ja: Const[str]
        en: Const[str]

    class PathName(NamedTuple):
        name: Const[str]

        @property
        def path(self) -> Const[Path]:
            return const(Path(self.name.get))


const = _DefineConst()


class Consts:
    # --------------------------------------------------
    # 汎用
    # --------------------------------------------------

    class Regex:
        PHONE_NUMBER = const(r"0\d{1,4}-\d{1,4}-\d{4}")
        POSTAL_CODE = const(r"\d{3}-\d{4}")
        EMAIL = const(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

    class Format:
        class Date:
            DATE = Structs.Format.Date(
                ja=const("%Y年%m月%d日"),
                slash=const("%Y/%m/%d"),
                hyphen=const("%Y-%m-%d"),
                dot=const("%Y.%m.%d"),
            )
            DATETIME = Structs.Format.Date(
                ja=const("%Y年%m月%d日 %H時%M分%S秒"),
                slash=const("%Y/%m/%d %H:%M:%S"),
                hyphen=const("%Y-%m-%d %H:%M:%S"),
                dot=const("%Y.%m.%d %H:%M:%S")
            )

    class Month:
        JAN = Structs.Translate(en=const("January"), ja=const("1月"))
        FEB = Structs.Translate(en=const("February"), ja=const("2月"))
        MAR = Structs.Translate(en=const("March"), ja=const("3月"))
        APR = Structs.Translate(en=const("April"), ja=const("4月"))
        MAY = Structs.Translate(en=const("May"), ja=const("5月"))
        JUN = Structs.Translate(en=const("June"), ja=const("6月"))
        JUL = Structs.Translate(en=const("July"), ja=const("7月"))
        AUG = Structs.Translate(en=const("August"), ja=const("8月"))
        SEP = Structs.Translate(en=const("September"), ja=const("9月"))
        OCT = Structs.Translate(en=const("October"), ja=const("10月"))
        NOV = Structs.Translate(en=const("November"), ja=const("11月"))
        DEC = Structs.Translate(en=const("December"), ja=const("12月"))

    class Week:
        MON = Structs.Translate(en=const("Monday"), ja=const("月曜日"))
        TUE = Structs.Translate(en=const("Tuesday"), ja=const("火曜日"))
        WED = Structs.Translate(en=const("Wednesday"), ja=const("水曜日"))
        THU = Structs.Translate(en=const("Thursday"), ja=const("木曜日"))
        FRI = Structs.Translate(en=const("Friday"), ja=const("金曜日"))
        SAT = Structs.Translate(en=const("Saturday"), ja=const("土曜日"))
        SUN = Structs.Translate(en=const("Sunday"), ja=const("日曜日"))

    class Season:
        SPRING = Structs.Translate(en=const("Spring"), ja=const("春"))
        SUMMER = Structs.Translate(en=const("Summer"), ja=const("夏"))
        AUTUMN = Structs.Translate(en=const("Autumn"), ja=const("秋"))
        WINTER = Structs.Translate(en=const("Winter"), ja=const("冬"))

    class Status:
        OK = const("OK")
        ERROR = const("ERROR")
        WARNING = const("WARNING")

    class Extension:
        EXCEL = const("xlsx")
        CSV = const("csv")
        JSON = const("json")
        YAML = const("yaml")
        YML = const("yml")
        TXT = const("txt")
        XML = const("xml")
        PDF = const("pdf")
        PNG = const("png")
        JPG = const("jpg")
        GIF = const("gif")
        MP4 = const("mp4")
        WAV = const("wav")
        ZIP = const("zip")
        DAT = const("dat")
        DAT = const("dat")
        PKL = const("pkl")
        PTH = const("pth")

    class Encoding:
        UTF8 = const("utf-8")
        UTF16 = const("utf-16")
        SHIFT_JIS = const("shift-jis")
        EUC_JP = const("euc-jp")

    class Delimiter:
        COMMA = const(",")
        TAB = const("\t")
        SPACE = const(" ")

    class LineFeed:
        CRLF = const("\r\n")
        LF = const("\n")

    class OS:
        WINDOWS = const("windows")
        MAC = const("mac")
        LINUX = const("linux")

    class MAX:
        INT = const(sys.maxsize)
        FLOAT = const(sys.float_info.max)

    # --------------------------------------------------
    # 学習モデル関連
    # --------------------------------------------------

    class Optimizer:
        SGD = const("SGD")
        ADAM = const("Adam")
        ADAGRAD = const("Adagrad")
        ADADELTA = const("Adadelta")
        RMS_PROP = const("RMSprop")

    class Loss:
        MSE = const("MSE")
        MAE = const("MAE")
        RMSE = const("RMSE")
        R2 = const("R2")

    class Metric:
        ACCURACY = const("accuracy")
        PRECISION = const("precision")
        RECALL = const("recall")
        F1 = const("f1")

    class Layer:
        DENSE = const("Dense")
        CONV2D = const("Conv2D")
        MAX_POOLING2D = const("MaxPooling2D")
        FLATTEN = const("Flatten")
        LSTM = const("LSTM")
        GRU = const("GRU")
        BIDIRECTIONAL = const("Bidirectional")
        DROPOUT = const("Dropout")
        BATCH_NORMALIZATION = const("BatchNormalization")

    class Activation:
        RELU = const("relu")
        SIGMOID = const("sigmoid")
        SOFTMAX = const("softmax")
        TANH = const("tanh")
        LINEAR = const("linear")

    class Padding:
        SAME = const("same")
        VALID = const("valid")

    class Pooling:
        MAX = const("max")
        AVG = const("avg")

    # --------------------------------------------------
    # ファイルパス
    # --------------------------------------------------
    class PathName:
        PARENT = Structs.PathName(const(".."))
        DATASET = Structs.PathName(const("dataset"))
        REPORTS = Structs.PathName(const("reports"))
        MODELS = Structs.PathName(const("models"))
        LOGS = Structs.PathName(const("logs"))
        KEYS = Structs.PathName(const("keys"))

    # --------------------------------------------------
    # AWS
    # --------------------------------------------------
    class AWS:
        class S3:
            class Minio:
                ACCESS_KEY = const("minioadmin")
                SECRET_KEY = const("minioadmin")
                ENDPOINT = const("localhost:9000")
                REGEON = const("us-east-1")


__all__ = ['const', 'Const', 'Consts']
