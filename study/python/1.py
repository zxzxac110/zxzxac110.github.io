# Series对象的生成和访问

import numpy as np
import pandas as pd

s = pd.Series([-1.55666192, -0.75414753, 0.47251231, -
              1.37775038, -1.648994421], index=['a', 'b', 'c', 'd', 'e'])
"""
输出
a   -1.556662
b   -0.754148
c    0.472512
d   -1.377750
e   -1.648994
dtype: float64
"""

s = pd.Series(["a", -0.75414753, 0.47251231, -1.37775038, -
              1.648994421], index=['a', 'b', 'c', 'd', 'e'])
"""
输出
a           a
b   -0.754148
c    0.472512
d   -1.377750
e   -1.648994
dtype: object
"""

s = pd.Series({'a': -1.55666192, 'b': -0.75414753, 'c': 0.47251231, 'd': -1.37775038, 'a': -
              1.648994421}, index=['a', 'b', 'c', 'd', 'e'])
"""
a   -1.648994 
b   -0.754148 
c         NaN 
d         NaN 
e         NaN 
dtype: float64
"""

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s = pd.Series({'a': 1, 'b': 2})
s = pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])  # 结果都是5
print(s)

print(s.values)
print(s.index)
print(s['a'])
print(s[['a', 'b']])
print(s[1:3])  # 第一个到三个之间的数,
