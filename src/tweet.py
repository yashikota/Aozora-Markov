import tweepy
from dotenv import load_dotenv
import os
import markovify


# 文章生成
def gen_sentence(parsed_text):
    STATE_SIZE = 5
    model = markovify.NewlineText(parsed_text, state_size=STATE_SIZE)
    sentence = None

    # 文が生成されるまで繰り返し
    while sentence == None:
        try:
            sentence = model.make_short_sentence(140)
        except Exception as e:
            print(e)

    sentence = "".join(sentence.split())

    return sentence


def tweet(sentence):
    # 環境変数の読み込み
    load_dotenv()
    client = tweepy.Client(bearer_token=os.environ["BT"], consumer_key=os.environ["CK"],
                           consumer_secret=os.environ["CS"], access_token=os.environ["AT"],
                           access_token_secret=os.environ["AS"])

    # ツイートする
    client.create_tweet(text=sentence)


def main(parsed_text):
    sentence = gen_sentence(parsed_text)

    tweet(sentence)


if __name__ == "__main__":
    main(str)
