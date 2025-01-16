import pandas as pd 

df = pd.read_csv("C:\\Academics\\Machine-Learning\\Libraries\\pandas\\taxi_zones.csv")
# print("Top-5:\n")
# print(df.head())
# print("Bottom-5:\n") 
# print(df.tail())

# print(df['Latitude']==42.307797 )

# print(df.drop('OBJECTID',axis=1,inplace=True))  #permanent deletion of a column
# print(df.describe()) 
df['OBJECTID']=df['OBJECTID']+1
print(df)