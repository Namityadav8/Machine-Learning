def sq(a):
    return a*a
num=[1,2,3,4,5,6,7,8,9]

a=list(map(sq,num))
for i in a:
    print(i,end=" ")



#We can also use lambda function in map
print("")
a=list(map(lambda x:x*x,num))
for i in a:
    print(i,end=" ")