import os
import parse
import tweet
import dir
import download
import prep


def main():
    # ディレクトリの変更
    YEAR = "2021"
    dir.main(YEAR)

    # input.txtがなければ作成
    if not os.path.exists("input.txt"):
        download.main(YEAR)
        prep.main()

    # 投稿
    parsed_text = parse.main()
    tweet.main(parsed_text)


if __name__ == "__main__":
    main()
