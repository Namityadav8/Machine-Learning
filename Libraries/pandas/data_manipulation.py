import pandas as pd 


df['sales']=df['salesfill'].fillna(df['sales'].mean())   #filling zero values of a column 
                                                        # with the mean of the column

#renaming colums

df.rename({"sales":{"sales1"}}) #renaming a column from sales to sales1

#changing data type of a column   (Make sure to know new column will be created)
df['new_sales']=df['sales'].astype(int)

## if there is na values in the column then we can fill it with the mean of the column
df['new_sales']=df['sales'].fillna(df['sales'].mean()).astype(int)



#applying function to the columns
df['new_sales']=df['sales'].apply(lambda x:x*3)



#aggreagation and grouped functions

grouped_mean=df.groupby('store')['sales'].mean()  #mean of sales for each store


#aggregation with multiple functions
grouped_mean=df.groupby('store')['sales'].agg(['mean','sum','count']) 


#Merging two dataframes
df1=pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
df2=pd.DataFrame({'A':[7,8,9],'B':[10,11,12]})







