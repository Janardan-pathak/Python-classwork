""" WAP that takes two values from user and return devision of first form second"""


def devide(a, b):
    return a / b


a = int(input("input first value: "))
b = int(input("input second value: "))

print(f"Devision of {a}/{b} is {devide(a,b)}")
