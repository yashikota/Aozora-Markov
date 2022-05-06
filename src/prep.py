import os
from tqdm import tqdm
import unicodedata
import re


# ファイルを変換
def convert_files():
    PRE_PATH = "./txt/"
    POST_PATH = "./etl_txt/"

    # ディレクトリがなければ作成
    if not os.path.exists(POST_PATH):
        os.mkdir(POST_PATH)

    # ファイル一覧を取得
    files = os.listdir(PRE_PATH)

    # 本文だけを抽出、shift_jisからutf-8に変換
    for file in tqdm(files, desc="変換"):
        try:
            with open(PRE_PATH + file, "r", encoding="shift_jis") as f:
                text = f.read()
                normalized_text = normalize_text(text)
            with open(POST_PATH + file, "w", encoding="utf-8") as f:
                f.write(normalized_text)
        except Exception as e:
            print(e, file)
            continue


# 本文だけを抽出
def normalize_text(text):
    try:
        text = unicodedata.normalize("NFKC", text)  # 全角を半角に変換
        text = re.split(r"\-{5,}", text)[2]  # 2つ目の---より後ろの部分を取得
        text = re.split(r"底本:", text)[0]  # 底本：より前の部分を取得
        # 《 》に囲まれた部分、[ ] に囲まれた部分、( ) に囲まれた部分、| 、半角スペースを削除
        text = re.sub(r"《.*?》|\[.*?\]|\(.*?\)|\|| ", "", text)
        text = text.strip()  # 不要な改行を削除
    except Exception as e:
        print(e)

    return text


# 1つのテキストファイルに結合
def merge_text():
    DIR_PATH = "./etl_txt/"
    FILE_NAME = "input.txt"
    files = os.listdir(DIR_PATH)

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for file in tqdm(files, desc="結合"):
            with open(DIR_PATH + "/" + file, "r", encoding="utf-8") as f2:
                f.write(f2.read())


def main():
    # ファイルを変換
    convert_files()

    # 1つのテキストファイルに結合
    merge_text()


if __name__ == "__main__":
    main()
