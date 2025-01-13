# try:
#     a=b
# except NameError as e:
#     print(f"the error is {e}")
# else:
#     print("try executed without any error")
# finally:
#     print("This will run no matter what")

a=int(input("Enter a number: "))
try:
    a=1/12
# except ModuleNotFoundError as e1:
#     print(e1)
# except NameError as e2:
#     print(e2)
except ZeroDivisionError as e:
    print(e)

else:
    print(f"no exception and the result is {a}")
finally:
    print("this is for fun it doesnt have any effect on the code")