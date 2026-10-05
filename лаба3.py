#3.2.1. Функції з параметрами
def multiply(a, b):
    sum = a + b     #додавання чисел
    return sum      #повернення значення

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

res = multiply(a, b)
print("Сума чисел = ", res)

# 3.2.2. Lambda-функції
nums = [5, 6, 12, 5.45, 15, -2]
sorted_numbers = sorted(nums, key = lambda x:x)     #Сортування значень
print(sorted_numbers)                               #-2, 5 , 5.45, 6, 12, 15

# 3.2.3. Функції з необов’язковими параметрами
def greet(name, greeting='Привіт'):        #greeting - за замовчуванням = "Привіт"
    return greeting + ', ' + name

print(greet("Влад", "Привіт"))
print(greet("Влад"))

# 3.2.4. Комбіноване завдання
check_numbers = lambda x:x % 2 == 0     #функція для визначення парності

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

if check_numbers(num1) and check_numbers(num2):     #перевірка парності чисел
    print("Числа є парними")
else:
    print("Є не парне число")