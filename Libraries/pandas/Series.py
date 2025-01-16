import pandas as pd 




# a=[1,2,3,4,5]
# data=pd.Series(a)
# print(data)


#creating a series from a dictionary
# data={'a':1,'b':2,'c':3}
# x=pd.Series(data)
# print(x)


#creating a series by giving custom data for index
data=[1,2,3,4,5]
index=['a','b','c','d','e']
series=pd.Series(data,index)
print(series)



data={'a':1,'b':2,'c':3}
# x=pd.Series(data)
# print(x)