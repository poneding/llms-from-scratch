import re


class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]

        preprocessed = [
            item if item in self.str_to_int else "<|unk|>" for item in preprocessed
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # 移除特定标点符号前的空格
        text = re.sub(r'\s+([,.?!"()\'])', r"\1", text)
        return text


def main():
    pass


if __name__ == "__main__":
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        text = f.read()
    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    preprocessed = [item for item in preprocessed if item.strip()]
    print(len(preprocessed))

    print(preprocessed[:100])

    all_tokens = sorted(set(preprocessed))
    all_tokens.extend(["<|endoftext|>", "<|unk|>"])
    vocab_size = len(all_tokens)
    print(vocab_size)

    vocab = {token: index for index, token in enumerate(all_tokens)}
    for i, item in enumerate(vocab.items()):
        print(item)
        if i >= 50:
            break
    tokenizer = SimpleTokenizerV1(vocab)
    text = """It's the last he painted, you know, Mrs. Gisburn said with pardonable pride."""
    ids = tokenizer.encode(text)
    print(ids)

    print(tokenizer.decode(ids))

    text1 = "Hello, do you like tea?"
    text2 = "In the sunlit terraces of the palace."
    text = "<|endoftext|> ".join([text1, text2])
    print(text)

    print(tokenizer.encode(text))
    print(tokenizer.decode(tokenizer.encode(text)))
