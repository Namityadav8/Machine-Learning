import sys
#counting reference count of a variable
a=[]  # one is refered here
print(sys.getrefcount(a))  #another one is here  

del a 
print(sys.getrefcount(a))