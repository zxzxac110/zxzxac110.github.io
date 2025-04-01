# 爬取table数据 导出为csv格式

import pandas as pd
import requests

url = 'http://www.kuaidaili.com/free/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)
dfs = pd.read_html(response.text)  # 所有table list 格式

# 爬取的数据
print(dfs[0])
df = dfs[0]
print(type(df))

# df.to_csv('名称.csv', mode='w', encoding='utf_8_sig', header=2, index=2)
# mode='a': 写入模式为追加模式，即如果文件已经存在，则在文件末尾追加写入内容
# encoding='utf_8_sig': 文件编码格式为UTF-8带BOM，这是为了在Excel中打开csv文件时避免中文乱码
# 常见的写入模式有以下几种：
# 'w'：写入模式，会覆盖已有的文件内容。
# 'a'：追加模式，不会覆盖已有的文件内容，在文件末尾追加新的内容。
# 'x'：创建模式，只有在文件不存在时才能创建新文件并写入内容。
# 'wb'、'ab'、'xb'：二进制写入模式，用于写入二进制数据。
# header=5: 写入csv文件时，从DataFrame的第5行开始写入列名
# index=4: 写入csv文件时，从DataFrame的第4行开始写入数据，即忽略前3行的数据

# 保存到本地，csv格式，注意中文编码：utf_8_sig
df.to_csv('名称.csv', mode='w', encoding='utf_8_sig', header=2, index=2)
