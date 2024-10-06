import math

a = 0.2
b = 0.3
h = 0.01
d = 10 ** -6

x = a

while x <= b:
    sum = 0
    k = 0
    calc = (1 / (4 * k + 3)) * x ** (4 * k + 3)
   
    while abs(calc) > d:
        calc = abs((1 / (4 * k + 3)) * x ** (4 * k + 3))
        sum += calc
        k += 1
    
    print(f"x = {x}; Result: {sum}")
  
    x += h
    x = round(x, 6)
