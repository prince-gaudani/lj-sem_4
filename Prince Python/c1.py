# read csv file
import pandas as pd
df=pd.read_csv('auto-mpg.csv')
print(df)

# print(df.head()) 
# # without argu in head first 5 row will be displayed by default

# print(df.head(8))
# # here first 8 row will be displayed

# print(df.tail())
# # without argu in tail last 5 row will be displayed by default

# print(df.columns)
# print(df.shape)

# Loc Function 
# print(df.loc[16:22])
# here end point in slicing incluided

# print(df["mpg"])

# print(df[["mpg"]])
# 2d form
# proper form in 2d form

# print(df[["mpg","cylinders","displacement"]])

# data for last five column's last 10 row
# print(df[["weight","acceleration","model year",'origin','car name']].tail(10))

# slicing in last 5 columns
# print(df[["weight","acceleration","model year",'origin','car name']].loc[199:207])

# ILoc function
print(df.iloc[11:33:3,2::2])
#  [,] in this first slicing for row and second for column and here end point is end-1

