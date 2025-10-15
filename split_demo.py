import re

text = "Hello, world. This, is a test."
result = re.split(r'([,.:;?_!"()\']|\s)', text)  # 分割成单词和标点符号
result = [item.strip() for item in result if item.strip()]  # 去除空字符串
print(result)
