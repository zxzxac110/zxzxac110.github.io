# csv文件读取

import numpy as np
import pandas as pd

# header 默认为0  从哪一行开始， 'None'的时候会有个索引开头 0  1 2 3, 非必须
# names=range(2, 5) 索引开头变为 2，3，4 位数和数据列数-1相符，非必须
# index_col 那一列是行索引, 行索引会移至最左侧
# # encoding 文件格式

# 已如下数据为例
"""
16888888888      张三      张三      张三
16888878888     张三5     张三5     张三5
12345678910  123546  123546  123546
12345678710     张三6     张三6     张三6
12345678716     张三7     张三7     张三7
12345608716     张三8     张三8     张三8
13345608716     张三9     张三9     张三9
"""
csv = pd.read_csv('C:/Users/东塘第一帅/Desktop/导入学员模板.csv', header=0, names=range(2, 5), index_col=1, encoding='ANSI')
print(csv)
