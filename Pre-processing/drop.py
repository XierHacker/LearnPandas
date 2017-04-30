import numpy as np
import pandas as pd


df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})
print("original:\n",df)

#get1接受的是第0行（因为这个时候axis=0）移除之后的新对象
#因为inplace默认是False，所以df不会有变化
get1=df.drop(labels=0)
print("df:\n",df)
print("get1:\n",get1)

#因为inplace这时候是True，所以df会变化，同时get2接受的是None值
get2=df.drop(labels=0,inplace=True)
print("df:\n",df)
print("get1:\n",get2)

#这个时候是移除列了，对比上面来看
get3=df.drop(labels="A",axis=1)
print("df:\n",df)
print("get3:\n",get3)