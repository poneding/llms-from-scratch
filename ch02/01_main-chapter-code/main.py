with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
print("Total number of character:", len(raw_text))
print(raw_text[:99])

import re

# text = "hello, world. This, is  a test."
# result = re.split(r"([,.]|\s)", text)
# result = [item for item in result if item.strip()]  # 去除空白字符串项
# print(result)

# text = "Hello, world. Is this-- a test?"
# result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
# result = [item for item in result if item.strip()]
# print(result)

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item for item in preprocessed if item.strip()]
print(len(preprocessed))
print(preprocessed[:30])

# 将词元转换维词元ID
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)

vocab = {token: i for i, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break

from tokenizer_v1 import SimpleTokenizerV1

tokenizer = SimpleTokenizerV1(vocab)
text = """"It's the last he painted, you know,"
       Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)

print(tokenizer.decode(ids))
