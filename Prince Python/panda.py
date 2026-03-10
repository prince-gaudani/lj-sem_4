# Pandas series 

# 1D data

import pandas as pd

# marks=[85,90,78,65]
# s=pd.Series(marks,index=['maths','python','fsd','dm'])
# print(s)

# marks=[85,90,78,65]
# s=pd.Series(marks)
# print(s)

# create series by using tupple
# t=('a','b','c')
# s=pd.Series(t)
# print(s)

# create series by using dictionary
# d={'a':10,'b':20,'c':30}
# d1=pd.Series(d)
# print(d1)

# create series by using array
# import numpy as np
# a=np.array([40,50,60])
# b=pd.Series(a)
# print(b)


# 2D data - Data frame
# create data frame by using dictionary
# d={'name':["prince",'smit','savan'],'marks':[45,78,56],'city':['ahm','surat','baroda']}
# df=pd.DataFrame(d)
# print(df)

# create dataframe by using list
# data=[['A',80],['B',90],["C",89]]
# df=pd.DataFrame(data,columns=['Name',"Marks"],index=[10,20,30])
# print(df)

# create dataframe by using list of dictionary
# data=[{"name":"A","marks":80},{"name":"B","marks":90}]
# df=pd.DataFrame(data,index=[1,2])
# print(df)

# create dictionary by using pandas series 
s1=pd.Series([1,2,3])
s2=pd.Series([8,9,10])
df=pd.DataFrame({"col1":s1,"col2":s2})
print(df)
print(df.set_index('col1'))

