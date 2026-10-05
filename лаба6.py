import os
people = []
users = {}

# 6.2.1 Операції зі списком чисел
# Створює список від 1 до 10
number_list = list(range(1, 11))

# Додає до списку число 11
number_list.append(11)

# Видаляє число 5 зі списку
number_list.remove(5)

# Сортує в звортньому порядку
number_list.sort(reverse = True)
print(number_list)  # Результат = [11, 10, 9, 8, 7, 6, 4, 3, 2,1]

# Завантаження повної інформації про користувача
def load_info():
    users = {}
    try:
        with open("people.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(", ")

                name = parts[0]
                data = {}

                for item in parts[1:]:
                    if ":" in item:
                        k, v = item.split(":", 1)
                        k = k.strip()
                        if isinstance(v, str):
                            v = v.strip()
                        try:
                            if "." in v:
                                v = float(v)
                            else:
                                v = int(v)
                        except:
                            pass
                        
                        data[k] = v
                users[name] = data                
    except FileNotFoundError:
        print("Файл ще не створено.")

    return users

# Перезапис інформації про користувача
def rewrite_file(users):    
    with open("people.txt", "w", encoding="utf-8") as file:
        for name, data in users.items():
            extra = ", ".join([f"{k.strip()}: {str(v).strip()}" for k, v in data.items()])
            file.write(f"{name}, {extra}\n")


users = load_info()
# 6.2.2 Робота зі словником
while True:
    print("1.Записати інформацію")
    print("2.Переглянути інформацію")
    print("3.Змінити інформацію")
    print("4.Видалити користувача")
    print("5.Додати інформацію")
    print("6.Завершити роботу")

    choice = input("Виберіть дію: ")

    # Запис данних користувача
    if choice == "1":
        name = input("Вкажіть ім'я: ")
        try:
            age = int(input("Вкажіть вік: "))
        except ValueError:
            print("Введіть число!")
            continue
        specialty = input("Введіть спеціальність: ")
        
        if not name or not specialty:
            print("Поле не може бути пустим.")
            continue

        users[name] = {
            'age':age,
            'specialty':specialty
        }
        print("Інформацію записано.")
        rewrite_file(users)

    # Перегляд данних користувача
    elif choice == "2":
        users = load_info()

        if not users:
            print("Інформації немає.")
            continue

        print("----Список користувачів----")
        names = list(users.keys())

        for i, name in enumerate(names, 1):
            print(f"{i}. {name}")

        print("\n1.Переглянути одного користувача")
        print("2.Переглянути всіх користувачів")

        sub_choice = input("Виберіть опцію: ")

        if sub_choice == "1":
            try:
                index = int(input("Оберіть користувача: ")) - 1
                name = names[index]
            except (ValueError, IndexError):
                print("Невірний вибір.")
                continue

            data = users[name]
            info = ", ".join([f"{k.strip()}: {str(v).strip()}" for k, v in data.items()])

            print(f"\n{name} | {info}\n")

        elif sub_choice == "2":
            print("----Всі користувачі:----")
            for i, (name, data) in enumerate(users.items(), 1):
                info = ", ".join([f"{k.strip()}: {str(v).strip()}" for k, v in data.items()])
                print(f"{i}. {name} | {info}")
        else:
            print("Невірний вибір.")

    # Зміна інформації користувача
    elif choice == "3":
        users = load_info()
        names = list(users.keys())

        for i, name in enumerate(names, 1):
            print(f"{i}. {name}")

        try:
            index = int(input("Оберіть користувача: ")) - 1
            name = names[index]
        except (ValueError, IndexError):
            print("Невірний вибір.")
            continue

        if not users:
            print("Інформації немає.")
            continue

        print(f"Редагуєш данні користувача: {name}")
        
        fields = list(users[name].keys())

        for i, (k, v) in enumerate(users[name].items(), 1):
            print(f"{i}. {k.strip()}: {str(v).strip()}")

        index = int(input("Оберіть поле: ")) - 1
        key = fields[index]

        value = input("Нове значення: ")

        try:
            value = float(value)
            if value.is_integer():
                value = int(value)
        except:
            pass

        users[name][key] = value
        rewrite_file(users)        

    # Видалення користувача
    elif choice == "4":
        users = load_info()

        # Перевірка чи є інформація в файлі
        if not users:
            print("Інформації немає.")
            continue
        else:
            print("----Список користувачів----")
            names = list(users.keys())

            for i, name in enumerate(names, 1):
                print(f"{i}. {name}")

            print("\n1.Видалити одного користувача")
            print("2.Видалити всіх користувачів")

            sub_choice = input("Виберіть опцію: ")

            if sub_choice == "1":
                try:
                    index = int(input("Оберіть користувача, щоб видалити: ")) - 1
                    name = names[index]
                # Виведення помилки,якщо введено не цифри
                except (ValueError, IndexError):
                    print("Невірний вибір.")
                    continue

                # Видалення користувача з файлу(списку)
                del users[name]
                # Перезапис інформації в файлі
                rewrite_file(users)

                print(f"Користувача {name} успішно видалено.\n")

            elif sub_choice == "2":
                print("Ви впевненні,що хочете видалити всіх?:")
                answer = input("Так або Ні:")

                if answer == "так":
                    print("Всіх користувачів було успішно видалено.")

                    # Очистка всього списку
                    users.clear()
                    # Перезапис інформації в файлі
                    rewrite_file(users)

                elif answer == "ні":
                    print("Операцію відхилено")

                else:
                    print("Невірно введено")

    # Додавання нової інформації про користувача
    elif choice == "5":
        users = load_info()

        if not users:
            print("Інформації немає.")
            continue

        names = list(users.keys())

        for i, name in enumerate(names, 1):
            print(f"{i}. {name}")

        try:
            index = int(input("Оберіть користувача: ")) - 1
            name = names[index]
        except (ValueError, IndexError):
            print("Невірний вибір.")
            continue

        # Введення ключа інформації в список
        key = input("Введіть назву нового поля (наприклад середній бал): ")

        if key in users[name]:
            answer = input("Таке поле вже існує.Перезаписати?(так/ні): ")
            if answer.lower() != "так":
                print("Операцію скасовано.")
                continue
        # Введення значення ключа
        value = input("Введіть значення поля: ")

        # Перевірка чи новий ключ має цифри в значенні
        try:
            value = float(value)
            if value.is_integer():
                value = int(value)
        except:
            pass

        # Перезапис інофрмації
        users[name][key] = value
        rewrite_file(users)

        print("Інформацію успішно додано.")

    # Завершення роботи
    elif choice == "6":
        print("Дякую за користування")
        break

    # Виведення помилки про невірний номер
    else:
        print("Невірний номер")
        continue

# 6.2.3 Операції з множинами парних і непарних чисел

number_list1 = list(range(1, 11 ))  # Створення списку від 1 до 10
res1 = set(number_list1[1::2])      # Парні числа
res2 = set(number_list1[::2])       # Непарні числа

print("З\'єднання множий: ", res1 | res2)   # З'єднання множин = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("Перетин множин: ", res1 & res2)      # Перетин множин = set{}
print("Різниця множин: ", res1 - res2)      # Різниця між res1 до res2 = {2, 4, 6, 8, 10}
print("Різниця множин: ", res2 - res1)      # Різниця між res2 до res1 = {1, 3, 5, 7, 9}

# 6.2.4 Унікальні слова та сортування

word = []
while True:
    print("1.Додати слово до списку")
    print("2.Переглянути список")
    print("3.Сортувати список")
    print("4.Видалити слово")
    print("5.Вихід")

    choice = input("Виберіть дію: ")

    if choice == "1":
        # Введення інформації
        word_list = input("Введіть слово: ").strip()
        # Виведення помилки, що поле не може бути пустим
        if not word_list:
            print("Поле не може бути пустим")
            continue
        
        # Перевірка чи введена вище інформація мість цифри
        if any(char.isdigit() for char in word_list):
            print("Не можна вводити цифри")
            continue

        # Перевірка на наявність любого слова в списку
        if any(word_list.lower() == w.lower() for w in word):
            print("Данне слово вже існує")
            continue

        # Запис інформації в список
        word.append(word_list)
        print("Слово додано до списку")

    elif choice == "2":
        # Перевірка чи список не пустий
        if not word:
            print("Список пустий")
            continue
        # Виведення інформації зі списку
        print(f"Список слів:")
        for i, w in enumerate(word, start=1):
            print(f"{i}. {w}")

    elif choice == "3":
        # Перевірка чи список не пустий
        if not word:
            print("Список пустий")
            continue
        # Сортування списку
        word.sort()
        print("Список відсортовано")

    elif choice == "4":
        # Перевірка чи список не пустий
        if not word:
            print("Список пустий")
            continue
        # Виведення інформації зі списку
        print(f"Список слів:")
        for i, w in enumerate(word, start=1):
            print(f"{i}. {w}")
        # Перевірка,щоб було введено число
        try:
            delete_word = int(input("\nВиберіть слово,щоб видалити: "))
        except ValueError:
            print("Введіть число!")
            continue
        # Перевірка нумерації
        if 1 <= delete_word <= len(word):
            removed_word = word.pop(delete_word - 1)
            print(f"Слова '{removed_word}' видалено.")
        else:
            print("Невірний номер")
            continue

    elif choice == "5":
        # Завершення роботи
        print("Дякую за користування.")
        break

    else:
        print("Невірний номер")
        continue