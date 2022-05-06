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

## Misc

形態素解析は
[MeCab](https://github.com/taku910/mecab)
と
[UniDic](https://clrd.ninjal.ac.jp/unidic/)
を使用。  
マルコフ連鎖は
[Markovify](https://github.com/jsvine/markovify)
を利用。
