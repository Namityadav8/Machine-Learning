
def sum_all(*args):
    return sum(args)

print(sum_all(10, 20, 30))  # 60

def show_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_details(name="Namit", age=22, course="Java")
