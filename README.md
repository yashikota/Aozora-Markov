# Aozora Markov

[青空文庫](https://www.aozora.gr.jp)
の
[2021年テキスト版 アクセスランキング](https://www.aozora.gr.jp/access_ranking/2021_txt.html)
より上位500位の作品を形態素解析した後、マルコフ連鎖による文章生成を行い、1時間に1回
[Twitter](https://twitter.com/AozoraMarkov)
に投稿します。

## Usage

必要に応じてvenv作成してください。

```bash
pip install -r requirements.txt
```

UniDicをダウンロードします。

```bash
python3 -m unidic download
```

main.pyを動作させると一連の処理を自動で行い、文章を生成できます。

```bash
python3 ./main.py
```

各プログラムを個別に実行したい場合はディレクトリ移動してから

```bash
cd ./data/2021
```

ファイルを実行するようにしてください。

```bash
python3 ./output.py
```

## src

- bot.py
  - Botの運用
- dir.py
  - ディレクトリ移動
- download.py
  - 青空文庫からファイルを取得
- learn.py
  - 学習モデルの作成
- main.py
  - ダウンロードから文章の生成までを自動で行う
- output.py
  - 学習モデルより生成された文章を出力
- parse.py
  - 形態素解析により、入力されたテキストを分かち書きに
- prep.py
  - 学習に不要なルビや説明などを省くための前処理
- tweet.py
  - 生成された文章をツイート

## Misc

形態素解析は
[MeCab](https://github.com/taku910/mecab)
と
[UniDic](https://clrd.ninjal.ac.jp/unidic/)
を使用。  
マルコフ連鎖は
[Markovify](https://github.com/jsvine/markovify)
を利用。
