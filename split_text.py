import re

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    text = f.read()
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
preprocessed = [item for item in preprocessed if item.strip()]
print(len(preprocessed))

print(preprocessed[:100])

all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)

vocab = {token: index for index, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break
