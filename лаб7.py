# 7.2.1 Перевірка коректності вводу чисел
while True:
    """
    num = int(input) - введення числа користувачем
    break = завершує програму,якщо було введено число

    except ValueError: - виводить помилку про не вірність введення числа
    continue - продовжує роботу програми поки не буде введено число
    """
    try:
        num = int(input("Введіть число: "))
        print(f"Ваше число: {num}")
        break
    except ValueError:
        print("Введіть число!")
        continue

# 7.2.2 Робота з файлами
# Визначення, що файлу не існує
file = None

try:
    """
    file = open - спроба відкрити файл
    content = file.read - спроба прочитати, що всередені файлу
    
    except FileNotFoundError - виведення помилки про відсутність файлу
    file = open("w+") - записує інформацію в файл з створенням самого файлу
    file.write() - запис інформації в файл
    print() - вивід інформації, що файл створено

    finally: - виконує завжди операцію
    if file: - перевіряє значення файлу

    Якщо закоментувати:
    "file = None
    file = open("example.txt", "w+", encoding="utf-8")
    file.write("Привіт користувач")
    print("Файл створено.")"

    Буде вибивати помилку:
    File "d:\Проєкти Пітон\лаб7.py", line 52, in <module>
    if file:
       ^^^^
    NameError: name 'file' is not defined. Did you mean: 'filter'?
    
    Якщо тільки закоментувати тільки:
    "file = open("example.txt", "w+", encoding="utf-8")
    file.write("Привіт користувач")
    print("Файл створено.")"

    Помилки вибивати не буде.
    Буде виводити на екран інформацію,що файлу не існує

    file.close() - закриття файлу
    print("Файл закрито") - виведення інформації
    """
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Файлу не існує.")
    file = open("example.txt", "w+", encoding="utf-8")
    file.write("Привіт користувач")
    print("Файл створено.")
finally:
    if file:
        file.close()
        print("Файл закрито")

# 7.2.3 Створення власного виключення
# Створення класу виключення негативного значення числа
class NegativeNumberError(Exception):
    pass

"""
    def check_possitive(number): - функція перевірки числа(number)
    if number < 0 - перевірка чи число більше 0(позитивне)
    raise NegativeNumberError(клас) - виведення помилки
"""
def check_possitive(number):
    if number < 0:
        raise NegativeNumberError("Число не може бути від'ємним")

# Створення класу ліміту віку
class AgeLimitError(Exception):
    pass

"""
    def check_age(age): - функція перевірки віку(age)
    if age < 18 - перевірка чи є 18
    raise AgeLimitError(клас) - виведення помилки
    """
def check_age(age):
    if age < 18:
        raise AgeLimitError("Ваш вік має бути більше 18")

"""
    age = int(input) - Введення інформації користувачем
    check_age(age) - введення функції перевірки віку
    
    except AgeLimitError - виведення інформації про помилку
"""
try:
    age = int(input("Введіть ваш вік: "))
    check_age(age)
    print(f"Ваш вік: {age}")
except AgeLimitError as e:
    print(f"Помилка {e}")