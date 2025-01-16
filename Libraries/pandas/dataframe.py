import pandas as pd 


#Creating data frame using dictionary
# data ={
#     'Name':['Tom', 'Jerry', 'Mickey', 'Donald'],
#     'Age':[20, 21, 22, 23],
#     'City':['New York', 'California', 'Las Vegas', 'Florida']
# }
# df=pd.DataFrame(data)
# print(df)



#creating data frame from a list of dictionaries

data =[
    {'name':'Tom', 'age':20, 'city':'New York'},
    {'name':'Jerry', 'age':21, 'city':'California'},
    {'name':'Mickey', 'age':22, 'city':'Las Vegas'},
    {'name':'Donald', 'age':23, 'city':'Florida'}
]

df=pd.DataFrame(data)
print(df)