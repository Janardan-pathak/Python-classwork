def modify_immutable(x):
    x = +1
    print(f"Inside fuction: {x}")


a = 5
modify_immutable(a)
print(f"Outside function: {a}")


def modifu_mutable(lst):
    lst.append(4)
    print(f"Inside function: {lst}")


my_list = [1, 2, 3]

modifu_mutable(my_list)
print(f"Outside function: {my_list}")


def modify(x):
    print(f"before :{id(x)}")
    x += 1
    print(f"After: {id(x)}")


a = 5
modify(a)
