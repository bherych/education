import math

def first_func(x):
    return math.cos(math.log(x ** 2))

def second_func(x):
    return 1/math.cos(x ** 4)

def third_func(x):
    return math.tan(math.sin(x))

a = 2
b = 4
h = 0.2
x = a
result = []

while x <= b:
    if x < 2.5:
        result.append((x, first_func(x)))
    elif 2.5 <= x <= 3.5:
        result.append((x, second_func(x)))
    elif x > 3.5:
        result.append((x, third_func(x)))
    
    x += h
    x = round(x, 3)

for x, y in result:
    print(f"x = {x}; f(x) = {y};")
