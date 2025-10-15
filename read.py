with open("the-verdict.txt", "r", encoding="utf-8") as f:
    text = f.read()
print("Total number of character:", len(text))
print(text[:1000])  # 打印前1000个字符
