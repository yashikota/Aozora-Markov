import os

import dir
import download
import prep
import learn
import output
import parse


def main():
    # ディレクトリの変更
    YEAR = "2021"
    dir.main(YEAR)

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
