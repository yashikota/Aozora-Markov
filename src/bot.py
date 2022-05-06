import os
import parse
import tweet
import dir


def main():
    # ディレクトリの変更
    YEAR = "2021"
    dir.main(YEAR)

    # 投稿
    parsed_text = parse.main()
    tweet.main(parsed_text)


if __name__ == "__main__":
    main()
