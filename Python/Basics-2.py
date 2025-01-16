# a=[1,2,3,4]
# b=iter(a)
# print(next(b))
# print(next(b))

# def read_file(file_path):
#     with open(file_path,'r') as file:
#         for i in file:
#             yield i


a=[x for x in range(10)]     # List comprehension
print(a)