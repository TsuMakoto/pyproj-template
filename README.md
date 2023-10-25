# TIS 除雪経路最適化

## Requirement

Pipenvを利用

- python 3.10 over
- pipenv

# Installation

```bash
> pip install pipenv # ない場合

# or (pipenvからlockして生成しているので、未確認)

> pip install -r requirement.txt

> pipenv install

# or

> pipenv install --dev
```

## 構成について

```
.
├── config # 設定ファイルなどをおく
│   └── keys # 認証情報やAPI鍵など（コミットはしない）
├── datasets
│   ├── private # 先方からのデータなどを配置
│   └── public  # オープンなデータなどを配置
├── docs # 仕様・ドキュメントなど、コード管理すべきものを配置
├── gallery # データセットを利用したものや、実験コードを走らせるなど（main.pyを配置）
│   ├── simulation  # データを用いないもの
│   ├── use_private # privateデータを用いたもの
│   └── use_public  # publicデータを用いたもの
├── libs # pipからインストールできないものなど配置（独自汎化コードなど）
├── logs
├── models
├── mypy.ini
├── notebooks
│   ├── draft
│   └── publish
│       └── pack
├── reports # グラフや図など
├── src
│   ├── __init__.py
│   ├── base # 継承して、使いたいベースモジュールがあれば記載（必ずABCを継承させる)
│   │   ├── API
│   │   ├── ML
│   │   ├── database
│   │   ├── optim
│   │   └── web
│   │       ├── request
│   │       └── response
│   ├── core
│   │   ├── flow
│   │   │   ├── I # 各interfaceを配置(Protocolを継承)
│   │   │   │   └── __init__.py
│   │   │   │   # データロード=>データの処理=>モデリング=>評価の一連を定義してある
│   │   │   │   # 必ずしも利用しなくていいが、インターフェースが整うので意識する
│   │   │   ├── handler.py 
│   │   │   │   # intefaceを継承した値をそのまま返すクラス群が書いてある
│   │   │   └── identity.py
│   │   ├── helper # コード全体で利用できる汎用のコードを配置
│   │   │   └── decorators
│   │   │       └── tuple_to.py
│   │   │   # 基本的に定数のみ
│   │   │   # custom.pyの代わりに設定ファイルを置いて、読み込ませるようにしても良い
│   │   ├── settings
│   │   │   ├── custom.py
│   │   │   └── enums.py
│   │   ├── structs # 型定義のための構造体配置(Vector,Variable,Box,etc...)
│   │   │   ├── impl
│   │   │   └── typing.py
│   │   └── utils # pythonの標準組み込みのものを拡張させたい場合はここに
│   │       ├── __init__.py
│   │       └── iterable.py
│   ├── factory # インスタンス化コードを配置（いわゆるfactoryパターン）
│   │   └── __init__.py
│   ├── loaders # データのロードやパラメータのロード、設定のロードなど
│   ├── models  # モデリング
│   ├── processors # 前処理や後処理など、ドメイン固有の処理は基本的にここ
│   │   └── data
│   ├── runners    # loader,model,processorを組み合わせた汎用パイプラインを記述
│   │   └── base.py
│   └── services # 手続的な処理を汎化させたい場合はここ
├── tmp
└── tools # データ作成など、処理とは直接関係ないものをここ
```

### 解析や実験について

notebooks/に記載していく

- notebooks/draft
  ここには実験用コードを記載していく。
  
  基本的にはsrc/配下を参照せず、なるべく単品で動くものを置いていく方がいい。
  
  これだ！と思ったものができて、完成用のnotebookの作成が必要なら、publishへ移譲させる

- notebooks/publish
  完成用のnotebookを置く。納品用や公開用など色々
  
  src配下を参照して良いが、notebooks/publish/pack/配下に配置したnotebookのファイル名でtextファイルを置いて、コミット番号を記載しておく。
  
  もし、更新があった場合は、このテキストファイルの先頭に更新されたコミット番号を書いて更新する。
  
  よってここのコミットはnotebook単品で必ず行うこと
  
  例えば、
  1. notebooks/publish/A.ipynb # commit番号: xxyyzz
  2. notebooks/publish/pack/A.txt # 中身にxxyyzzを記載

### 構成について

詳しくはsrc/配下にそれぞれREADMEを置いているので参照
