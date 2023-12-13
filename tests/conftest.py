# conftest.py
import sys
from pathlib import Path

# プロジェクトのルートディレクトリにある仮定の 'src' ディレクトリを sys.path に追加
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))
