# DataFrame对象的生成和访问

import numpy as np
import pandas as pd

s = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
print(s)
"""
   a  b
0  1  3
1  2  4
"""


# 嵌套列表形式创建

s = pd.DataFrame([[1, 2, 3], [4, 5, 6]], index=['a', 'b'], columns=['as', 'bs', 'cs'])
print(s)
"""
   as  bs  cs
a   1   2   3
b   4   5   6
"""

# 二维ndArray形式创建
# i4 整数
# f4 浮点
# a10 字符串
#            行数量：2
data = np.zeros((2), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 1.5, 'asd'), (2, 2.5, 'asdf')]
s = pd.DataFrame(data, index=['1行', '2行'], columns=['C', 'A', 'cs'])
# columns默认为data.type,声明后则使用声明的
print(s)
"""
          C  A   cs
1行   b'asd'  1  NaN
2行  b'asdf'  2  NaN
"""

# 已Series创建
s = pd.Series(["a", -0.75414753, 0.47251231, -1.37775038, -
              1.648994421], index=['a', 'b', 'c', 'd', 'e'])
obj = {'one': s}
s = pd.DataFrame(obj)
# index默认为Series.index，columns默认为obj.key,声明后则使用声明的
print(s)
"""
        one
a         a
b -0.754148
c  0.472512
d  -1.37775
e -1.648994
"""

# 字典的字典形式创
user = pd.DataFrame([['张三', '男', 3], ['王二', '男', 6], ['刘大', '男', 6], ['李玲', '男']], index=['111', '222', '333', '444'], columns=['姓名', '性别', '年龄'])
df = pd.DataFrame({
    ('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
    ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
    ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
    ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
    ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}
})

# 查看
print('全部内容')
print(df)  # 全部内容
print(user)  # 全部内容
print('列标题')
print(df.index)  # 列标题（左）
print('行标题')
print(df.columns)  # 行标题（上）
print('所有内容值')
print(df.values)  # 所有值

print('某一列数据')
print(df[('a', 'b')])
print(user['姓名'])

print('某一/几行行数据')
print(df.loc[('A', 'B')])
print(user[1:2])  # 第一行到第二行的数据 不包括第一行
print(user[:])  # 所有行

print('某一/几个个数据')
# print(user.loc[:, ['姓名']])  # 所有行的姓名选项
# print(user.loc[['111'], ['姓名']])  # 111行的姓名选项
# print(df.loc[('A', 'B'), ('a', 'b')])  # AB行的ab选项
# print(user.iloc[0:1, 0:1])  # 第0-1行的第0-1列选项
# print(user.iloc[[0, 1], [0, 2]])  # 第0行和第1行的第0列和第2列选项
# print(user.loc[user['年龄'] > 1, ['姓名']])  # 年龄大于1的的姓名

print(user.head(1))  # 前一行数据
print(user.tail(1))  # 后1行数据

print('其他数据')
# print(user.shape[:])  # (2,3)  2行3列
# print(user.shape[0:1])  # 不是很懂
# print(user.describe())  # 获得整个table的统计数据 比如min max 平均数 样本标准差std
# print(user.info())  # 获得table的一些数据
# print(user.isnull())  # 返回数据 会将缺失数据转化成true显示
# print(user[user.isnull().T.any()])  # 返回 有缺失数据的所有行

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

"""
       a              b
       b    a    c    a     b
A B  1.0  4.0  5.0  8.0  10.0
  C  2.0  3.0  6.0  7.0   NaN
  D  NaN  NaN  NaN  NaN   9.0
"""
