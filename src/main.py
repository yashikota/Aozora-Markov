import os

import download
import prep
import learn
import output
import tweet
import parse


# ディレクトリの変更
def change_dir(year):
    # もしカレントディレクトリがsrcであれば1つ上のディレクトリに移動
    if os.path.basename(os.getcwd()) == "src":
        os.chdir("..")

    # dataディレクトリがなければ作成
    if not os.path.exists("data"):
        os.mkdir("data")

    # dataディレクトリに移動
    os.chdir("data")

    # カレントディレクトリをyearに変更し、ディレクトリがなければ作成
    if not os.path.exists("./" + year + "/"):
        os.mkdir("./" + year + "/")

    # カレントディレクトリをyearに変更
    os.chdir("./" + year + "/")


def main():
    # ディレクトリの変更
    YEAR = "2021"
    change_dir(YEAR)

    # input.txtがなければ作成
    if not os.path.exists("input.txt"):
        download.main(YEAR)
        prep.main()

    # model_data.jsonがなければ作成
    if not os.path.exists("model_data.json"):
        parsed_text = parse.main()
        learn.main(parsed_text)

    # 表示
    output.main()


if __name__ == "__main__":
    main()
