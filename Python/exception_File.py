try:
    a=open('file.txt','r')
    print(open)
except FileNotFoundError as e:
    print(e)
else:
    print("File is available ")
finally:
    if 'file' in locals() and not a.closed():
        a.close()
        print("File is clsoed")