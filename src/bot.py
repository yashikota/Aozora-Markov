import os
import parse
import tweet


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

    # 投稿
    parsed_text = parse.main()
    tweet.main(parsed_text)


if __name__ == "__main__":
    main()
