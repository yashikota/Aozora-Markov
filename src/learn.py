import markovify


# モデルデータを生成
def learn_markov(parsed_text):
    print("モデルを生成しています...")
    model = markovify.NewlineText(parsed_text, state_size=5)
    with open("model_data.json", "w", encoding="utf-8") as f:
        f.write(model.to_json())


def main(parsed_text):
    # モデルデータを生成
    learn_markov(parsed_text)


if __name__ == "__main__":
    main(str)
