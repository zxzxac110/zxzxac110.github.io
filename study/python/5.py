# DataFrame对象的填充和修改

import numpy as np
import pandas as pd
import requests
import datetime


user = pd.DataFrame([['张三', '男', 3], ['王二', '男', 6], ['刘大', '男', 6], ['李玲', '男']], index=['111', '222', '333', '444'], columns=['姓名', '性别', '年龄'])
# user.dropna 删除有缺少数据的列或行
# axis =0 删除有缺少数据的行  =1删除有缺少数据的列
# how= 'all' 所有内容都是缺失才删除  ='any'有一项确实缺失就删除
user2 = user.dropna(axis=1, how='all')
print(user2)

# user2.fillna 填充缺少数据
# method='ffill' 使用上一格数据填充  method='bfill'使用下一个数据填充
# axis =0 列方向填充 ， =1 行方向填充
# inplace 是否改变源数据
user2.fillna(method='ffill', axis=0, inplace=True)
print(user2)

# 精度操作
print('精度操作')
s = pd.DataFrame(
    [
        ['哈哈', 1.001, 1.0052, 3.0],
        ['哈哈', 2.001, 1.0052, 3.0],
        ['哈哈', 1.001, 1.0052, 3.0],
        ['哈哈', 0, 1.0052],
    ],
    columns=['姓名', '性别', '数值', '年龄']
)
s.fillna(method='ffill', axis=0, inplace=True)  # 填充数据 防止转整数时缺失数据报警

# 将数据转化成2位浮点数，年龄转化成整数
# 方法一
# s = s.applymap(lambda x: '%0.2f' % x)  # 对数据进行格式化操作，保留两位小数。返回的是字符串格式
# s['年龄'] = s.loc[:, ['年龄']].applymap(lambda x: '%0.0f' % x)
# print(s)

# 方法二
s.fillna(method='ffill', axis=0, inplace=True)  # 填充数据 防止转整数时缺失数据报警
s = s.round(2)
s['年龄'] = s['年龄'].astype(int)
print(s)

# 将为0的数据 取当前列的中间值填充
print(s[s['性别'] == 0])
print(s[s['性别'].isin([0])])  # 找到未性别为0的行
s.loc[s['性别'].isin([0]), '性别'] = s['性别'].median()  # ['性别'].describe().50%填充
print(s)
