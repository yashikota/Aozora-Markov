import os


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


def main(year):
    # ディレクトリの変更
    change_dir(year)


if __name__ == "__main__":
    main(int)
