import numpy as np
import pandas as pd


data1={"key":["b","b","a","c","a","a","b"],
       "num1":range(7)}
df1=pd.DataFrame(data=data1)

data2={"key":["b","b","d"],
       "num2":range(3)}
df2=pd.DataFrame(data=data2)
print(df1)
print(df2)