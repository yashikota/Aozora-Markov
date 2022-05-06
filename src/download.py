import requests
import re
from tqdm import tqdm
import os
import zipfile


#  URLリストを取得
def extract_url(literary_url):
    dl_url_list = list()

    # スクレイピング
    res = requests.get(literary_url)

    # www.aozora.gr.jp/cardsから始まるURLを抽出
    literary_url_list = re.findall(
        r"https://www.aozora.gr.jp/cards/.*/.*.html", res.text)

    for literary_url in tqdm(literary_url_list, desc="抽出"):
        res2 = requests.get(literary_url)

        # .zip"で終わるURLを抽出
        zip_url = (re.findall(r'/files/.*.zip"', res2.text))[0]
        pre = re.match(r"https://www.aozora.gr.jp/cards/\d*",
                       literary_url).group()

        # ダウンロードリンクのURLを作成
        dl_url = str(pre) + str(zip_url[:-1])
        dl_url_list.append(dl_url)

    # ファイルに保存
    with open("url_list.txt", "w") as f:
        for url in dl_url_list:
            f.write(url + "\n")

    return dl_url_list


# ダウンロード
def download_files(url_list):
    DIR_PATH = "./zip/"

    # ディレクトリがなければ作成
    if not os.path.exists(DIR_PATH):
        os.mkdir(DIR_PATH)

    # ダウンロード
    for url in tqdm(url_list, desc="ダウンロード"):
        # urlから\nを削除
        url = url.replace("\n", "")
        res = requests.get(url, stream=True)
        file_name = url.split("/")[-1]

        # もしファイルがあればスキップ
        if os.path.exists(DIR_PATH + file_name):
            continue

        with open(DIR_PATH + file_name, "wb") as f:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()


# 解凍
def unzip_files():
    DIR_PATH = "./txt/"
    ZIP_PATH = "./zip/"

    # ディレクトリがなければ作成
    if not os.path.exists(DIR_PATH):
        os.mkdir(DIR_PATH)

    # ZIPファイルを解凍
    for file_name in tqdm(os.listdir(ZIP_PATH), desc="解凍"):
        with zipfile.ZipFile(ZIP_PATH + file_name, "r") as zf:
            zf.extractall(DIR_PATH)

    # .txtファイル以外を削除
    del_files = [f for f in os.listdir(DIR_PATH) if not f.endswith(".txt")]
    for file in tqdm(del_files, desc="削除"):
        os.remove(DIR_PATH + file)


def main(year):
    # url_list.txtがあれば読み込み、なければ取得
    if os.path.exists("url_list.txt"):
        url_list = open("url_list.txt", "r").readlines()
        print("url_list.txtを読み込みました")
    else:
        url_list = extract_url(
            "https://www.aozora.gr.jp/access_ranking/" + year + "_txt.html")

    # ダウンロード
    download_files(url_list)

    # 解凍
    unzip_files()


if __name__ == "__main__":
    main(int)
