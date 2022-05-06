import markovify
import os
import learn
import parse


def gen_sentence():
    # モデルの読み込み
    with open("model_data.json") as f:
        model = markovify.NewlineText.from_json(f.read())
    print("model_data.jsonを読み込みました")

    # モデルから文章を生成
    sentence = None
    while sentence == None:
        try:
            sentence = model.make_short_sentence(140)
        except Exception as e:
            print(e)
    sentence = "".join(sentence.split())

    return sentence


def main():
    # model_data.jsonがあれば読み込み、なければ生成
    if os.path.exists("model_data.json"):
        print("model_data.jsonを読み込みます")
        sentence = gen_sentence()
    else:
        print("model_data.jsonがありません")
        parsed_text = parse.main()
        learn.main(parsed_text)
        print("model_data.jsonを生成しました")
        sentence = gen_sentence()

    # 表示
    print(sentence)
    print(len(sentence), "文字")


if __name__ == "__main__":
    main()
