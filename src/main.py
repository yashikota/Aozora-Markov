import os

import download
import prep
import learn
import output
import tweet
import parse


# ディレクトリの変更
def change_dir(year):
    # もしカレントディレクトリがprogramsであれば1つ上のディレクトリに移動
    if os.path.basename(os.getcwd()) == "programs":
        os.chdir("..")

    # カレントディレクトリをyearに変更し、ディレクトリがなければ作成
    if not os.path.exists("./" + year + "/"):
        os.mkdir("./" + year + "/")

    os.chdir("./" + year + "/")


def main():
    # ディレクトリの変更
    YEAR = "2021"
    change_dir(YEAR)

    # input.txtがなければ作成
    if not os.path.exists("input.txt"):
        download.main(YEAR)
        prep.main()

    # parsed_textを取得
    parsed_text = parse.main()

    # 表示
    learn.main(parsed_text)
    output.main()


if __name__ == "__main__":
    main()
