import math

# Створіть змінну `country` та присвойте їй назву вашої країни. Виведіть рядок, який містить назву країни.
country = "Ukraine"
print(country)

# Створіть змінну `age` та присвойте їй ваш вік. 
# Порівняйте вік з допустимим віком для вибору президента (35 років) та виведіть результат.
age = 25
if age >= 35:
    print("You are allowed to become the president of Ukraine")
else:
    print("You are too young to become the president of Ukraine")

# Створіть змінну `is_holiday` та присвойте їй значення `False`, а змінну `is_weekend` - значення `True`. 
# Виведіть результати логічних операцій. 
is_holiday = False
is_weekend = True

if is_holiday and is_weekend:
    print("It's a weekend holiday")

elif is_holiday or is_weekend:
    print("You can stay at home today")

else:
    print("You have to work today")

# Скласти програму згідно варіанту 4 з таблиці 2
x = 2.361
y = 1.149

result = (13 * x * y) + math.log(x / y) - 17 * math.sin(x ** 2 - y)
print(result)