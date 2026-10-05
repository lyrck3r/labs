# Імпорт модуля
import os

"""
    with open("file.txt", "w") as file: - відкриття файл для перезапису інформації
    for i in range(1, 11) - генерування чисел в діапазоні від 1 до 10(включно)
    file.write(str(i) + "\n") - запис чисел в файл, переносячи кожне число на новий рядок

    with open("file.txt", "r") as file: - відкриття файлу для читання інформації
    for line in file: - проходиться по кожному рядку файлу
    number = int(line.strip()) - прибирає зайві пробіли/переноси рядка і перетворює рядок у ціле число
    if number % 2 == 0 - перевіряє чи число парне(остача від ділення на 2 дорівнює 0)
    print(number) - якщо число парне, то виводить на екран
"""
with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(str(i) + "\n")

with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        if number % 2 == 0:
            print(number)

# Введення тексту користувачем
text = input("Введіть текст: ")

"""
    with open("file.txt", "w", encoding="utf-8") - відкриття файлу для запису інформації.
    - encoding="utf-8" - задає кодування для конкретного збереженого тексту(наприклад, українських символів)
    file.write(text) - записує інформацію від користувача в файл

    with open("file.txt", "r", encoding="utf-8") - відкриття файлу для читання інформації
    - encoding="utf-8" - задає кодування для конкретного збереженого тексту(наприклад, українських символів)
    content = file.read() - задає значення змінній "content", як читання файлу
"""
with open("users_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

with open("users_text.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Вирахування к-сті символів і рядків в файлі
char_count = len(content)
line_count = content.count("\n") + 1 if content else 0

# Вивведення інформації
print("Кількість символів: ", char_count)
print("Кількість рядків: ", line_count)

# Введення інформації від користуввача
filename = input("Введіть назву файлу: ")
ext = input("Введіть формат файлу: (txt, json) ")

"""
    class ExtentionError(Exception): - створення власного вийнятку "неправильний формат файлу"

    def check_ext(ext): - функція перевірки правильності формату файлу
    if ext not in ["txt", "json"] - перевірка на правильність формату
    raise ExtentionError - виведення помилки при невірності вказання формату
"""
class ExtentionError(Exception):
    pass

def check_ext(ext):
    if ext not in ["txt", "json"]:
        raise ExtentionError("Невірний формат.Підтримуються лише 'txt', 'json'")

"""
    Цикл створення і перейменування файлу

    check_ext(ext) - відразу ввожу функцію перевірки формату

    fullname = f"{filename}.{ext}" - записую нову змінну для повної назви файлу

    if os.path.isfile(fullname): - перевірка на наявність файлу за вказаною назвою
    new_name = f"{filename}_backup.{ext}" - нова назва перейменованого файлу
    os.rename(fullname, new_name) - перейменування файлу {fullname} на {new_name}
    print(f"Файл перейменовано на: {new_name}") - виведення інформації про перейменування

    with open(f"{fullname}, "w", encoding="utf-8") - відкриття файлу для запису інформації
    pass - нічого не виконує

    print(f"Файл створено. Назва файлу: {fullname}") - виводить інформацію про файл
    break - завершує програму

    except ExtentionError as e: - вивід власного вийнятку як помилку
    print(e) - виведення помилки
    ext = input("Спробуй ще раз: (txt, json)") - повторна спроба введення формату користувачем (працює,поки не введеться вірний формат)
"""
while True:
    try:
        check_ext(ext)
        
        fullname = f"{filename}.{ext}"

        if os.path.isfile(fullname):
            new_name = f"{filename}_backup.{ext}"
            os.rename(fullname, new_name)
            print(f"Файл перейменовано на: {new_name}")

        with open(f"{fullname}", "w", encoding="utf-8") as file:
            pass

        print(f"Файл створено. Назва файлу: {fullname}")
        break
    
    except ExtentionError as e:
        print(e)
        ext = input("Спробуйте ще раз: (txt, json) ")

# Введення інформацї користувачем
filename = input("Введіть назву файлу: ")
filename_backup = input("Введіть назву бек-ап файлу: ")
ext = input("Введіть формат файлів: (txt, json) ")

"""
    def check_file_exists(fullname): - функція перевірки на існування основного файлу з якого будуть копійовати данні
    if not os.path.exists(fullname) - перевірка на існування файлу
    print(f"Файлу '{fullname}' не існує) - виведення інформації про існування файлу
"""
def check_file_exists(fullname):
    if not os.path.exists(fullname):
        print(f"Файлу '{fullname}' не існує")
"""
    def copy_file(source, destination): - функція копійовання файлів(source - звідки, destination - куди)
    with open(source, "r", encoding="utf-8") as f_scr: - відкриття файлу для читання данних.позначенний як "f_scr"
    content = f_scr.read() - змінна для читання інформації з файлу

    with open(destination, "w", encoding="utf-8") as f_dst: - відкриття файлу для запису інформації.позначений як "f_dst"
    f_dst.write(content) - запис інформації на файл з іншого файлу
"""
def copy_file(source, destination):
    with open(source, "r", encoding="utf-8") as f_scr:
        content = f_scr.read()

    with open(destination, "w", encoding="utf-8") as f_dst:
        f_dst.write(content)

"""
    Цикл копіювання данних

    check_ext(ext) - перевірка формату файлів

    fullname = f"{filename}.{ext}" - назва основного файлу(з нього копіюємо данні)
    backup_fullname = f"{filename_backup}.{ext}" - назва бек-ап файлу(куди копіюємо данні)

    check_file_exists(fullname) - перевірка на наявність основного файлу

    copy_file(fullname, backup_fullname) - копіювання файлів з "fullname" в "backup_fullname"

    print(f"Данні файлу '{fullname}' успішно скопійовано в файл {backup_fullname}'")
    - виведення інформації про успішне копіювання даних з файлу "fullname" в "backup_fullname"
    - fullname = основний файл. backup_fullname = бек-ап файл
    break - завершення циклу/програми

    except ExtentionError as e: - вивід власного вийнятку як помилку
    print(e) - виведення помилки
    ext = input("Спробуй ще раз: (txt, json)") - повторна спроба введення формату користувачем (працює,поки не введеться вірний формат)

    except FileNotFoundError as e: - вивід вийнятку "файл не знайдено" як помилку
    print(e) - виведення помилки
    break - завершення програми

    except Exception as e: - вивід інших вийнятків, які можуть статись як помилку
    print("Сталась невідома помилка", e) - вивід інформації про помилку
    break - завершення програми
"""
while True:
    try:
        check_ext(ext)

        fullname = f"{filename}.{ext}"
        backup_fullname = f"{filename_backup}.{ext}"

        check_file_exists(fullname)

        copy_file(fullname, backup_fullname)

        print(f"Данні файлу '{fullname}' успішно скопійовані в файл '{backup_fullname}'")
        break

    except ExtentionError as e:
        print(e)
        ext = input("Не правильний формат. Введіть ще раз: (txt, json) ")
    
    except FileNotFoundError as e:
        print(e)
        break

    except Exception as e:
        print("Сталась невідома помилка", e)
        break