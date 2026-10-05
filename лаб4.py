# Імпорт математичного модуля і присвоєння псевдоніма
import math as m

# Обчислення квадратного значення довільного числа
number = float(input("Вкажіть число для обчислення квадратного коріня: "))
sqrt_value = m.sqrt(number)
print(f"Квадратний корінь числа {number} = {sqrt_value}")

# Обчислення кута в градусах
degrees = float(input("Введіть кут у градусах: "))

# Переведення градусів в радіанти
radian = m.radians(degrees)

# Обчислення синуса
sin_value = m.sin(radian)
print(f"Синус кута {degrees} = {radian}")

# Виведення значення числа π 
pi_value = m.pi
print("Значення числа π = {pi_value}")

# Імпорт конкретних функцій з модулів і присвоєння псевдонімів
from math import factorial as f
from random import randint as r

# Створення списку з числами
numbers = []

# Генерування 10 випадкових числе в діапазоні від 1 до 100
for i in range(10):
    num = r(1, 100)
    numbers.append(num)

# Виведення згенерованих чисел
print(f"Згенеровані числа:", numbers)

# Перевірка кожного числа, чи меньше воно за 10
# Обчислення факторіала чисел, які меньше 10
for num in numbers:
    if num < 10:
        fact = f(num)
        print(f"Факторіал числа {num} = {fact}")


# Імпорт конкретних функцій з модулів і присвоєння псевдонімів
from math import sqrt as root

# Імпорт модуля "random" і присвоєнян йому псевдоніма "rnd"
import random as rnd

# Генерування 5 випадкових чисел в діапазоні від 1 до 50
# Обчислення квадратного значення числа
# Виведення результату
for i in range(5):
    num = rnd.randint(1, 50)
    res = root(num)
    print(f"Число: {num}, Квадратний корінь: {res}")

