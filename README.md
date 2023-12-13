# python project template

## Requirement

Pipenvを利用

- python 3.10 over
- pipenv

```bash
> pip install pipenv

> pipenv sync

# use development packages
> pipenv install -d

```

## Use requirements.txt

```bash
> pip install -r requirements.txt

# use development packages
> pip install -r requirements.dev.txt

```

## Developments

Use Pipenv

```bash

> pip install pipenv

> pipenv shell

```

# test/linter/typing

```bash
# test
> pytest

# linter
> flake8 src tests gallery
> black --check src tests gallery

# typing
> mypy src

# full check
> tox
```

# 構成について

```
.
├── config   # 設定ファイルなど
│   └── keys        # 認証情報やAPI鍵など
├── datasets
│   ├── private     # 先方からのデータなど
│   └── public      # オープンなデータ
├── docs     # 仕様・ドキュメントなど
├── gallery  # データ等に基づくmain.pyを配置
│   ├── simulation  # データを用いないもの
│   ├── use_private # privateデータを用いたもの
│   └── use_public  # publicデータを用いたもの
├── libs     # pipからインストールできないものなど
├── logs
├── models
├── notebooks
│   ├── draft
│   └── publish
├── reports  # グラフや図など
├── src
│   ├── __init__.py
│   ├── base       # ベースモジュールの記載(ABCを継承)
│   ├── core
│   │   ├── helper     # コード全体で利用できる汎用のコードを配置
│   │   ├── settings   # 定数定義
│   │   ├── structs    # 型定義や構造体
│   │   └── utils      # pythonの標準組み込みのものを拡張させる場合
│   ├── factory    # factoryパターン
│   ├── loaders    # データのロードやパラメータのロード、設定のロードなど
│   ├── models     # モデリングコード
│   ├── processors # 前処理や後処理など、ドメイン固有の処理
│   ├── runners    # 汎用パイプライン
│   └── services   # 手続的な処理を記述
├── tmp
├── tools   # データ作成など、全体の処理とは直接関係ないもの
└── tests   # testing
```
