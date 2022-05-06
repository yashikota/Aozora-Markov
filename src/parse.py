import MeCab
import re
from tqdm import tqdm
import os
import sys


# 正規化
def normalization(texts):
    normalized_texts = list(str())

    for text in texts:
        normalized_texts.append(re.sub(
            '\'|\"|\(|\)|\[|\]|\r|<br />|\u3000|-|\||https?://[!\?/\+\-_~=;\.,\*&@#\$%\(\)\'\[\]]+|@[\\w]{1,15}', ' ', text))

    return normalized_texts


# 形態素解析
def parse_texts(normalized_texts):
    mecab = MeCab.Tagger("-Owakati")
    parsed_texts = str()

    for text in tqdm(normalized_texts, desc="パース"):
        parsed = mecab.parse(text)
        for token in parsed:
            if token == "\n":
                continue
            parsed_texts += token
            if token == "。":
                parsed_texts += "\n"

    # parsed.txtに保存
    with open("parsed.txt", "w", encoding="utf-8") as f:
        f.write(parsed_texts)

    return parsed_texts


def main():
    # parsed.txtがあれば読み込む
    if os.path.exists("parsed.txt"):
        parsed_text = open("parsed.txt", "r", encoding="utf-8").read()
        print("parsed.txtを読み込みました")

    # input.txtがない場合はエラー
    elif not os.path.exists("input.txt"):
        print("input.txtがありません。prep.pyを実行して生成してください")
        sys.exit()

    # input.txtがある場合は解析し、parsed.txtに保存
    else:
        texts = open("input.txt", "r", encoding="utf-8").readlines()
        parsed_text = parse_texts(normalization(texts))

    return parsed_text


if __name__ == "__main__":
    main()
