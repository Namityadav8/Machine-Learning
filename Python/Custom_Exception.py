class dobexception(Exception):
    pass

age=int(input("Enter your age: "))
try:
    if age>18 and age<30:
        print("You are eligible for the job")
    else:
        raise dobexception
except dobexception as dbe:
    print("You are not eligible for the job")   
    

    
    