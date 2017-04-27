import numpy as np
import pandas as pd

#对于一个Series来说,行数保持不变,列数变为不同类的个数
#但是每一行还是以编码的形式表示原来的类别
#这个函数返回是一个DataFrame,其中列名为各种类别
s = pd.Series(list('abca'))
print("original:")
print(s)
print("get dummy:")
s_dummy=pd.get_dummies(data=s)
print(s_dummy)
print("type of s_dummy:",type(s_dummy))


#############################

df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})
print("original:")
print(df)

#其中只要是类别相关的,都会被hot-encoding
#每一个特征(原始形式的列名)下面有几种不同的类别,就会生成几列(比如A下面只有a和b两种形式,就会生成A_a和A_b两列)
#原始为数字的那些特征,保持不变
#prefix表示你对于新生成的那些列想要的前缀,你可以自己命名
df_dummy=pd.get_dummies(data=df,prefix=["A","B"])
print("get dummy:")
print(df_dummy)