import os
import json
users = {}

def load_info():
    try:
        with open("people.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файла не існує.")
        return {}
    except json.JSONDecodeError:
        print("Файл пошкоджений.")
        return {}
    
def rewrite_file(users):
    with open("people.json", "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

users = load_info()
while True:
    print("========Меню========")
    print("1.Внести інформацію")
    print("2.Додати нову інформацію")
    print("3.Змінити інформацію")
    print("4.Переглянути інформацію")
    print("5.Видали користувача")
    print("6.Вихід")

    choice = input("Виберіть опцію: ")

    if choice == "1":
        name = input("Введіть ім'я: ").strip()
        
        if not name.replace(" ", "").isalpha():
            print("Ім'я має містити тільки букви")
            continue

        try:
            age = int(input("Вкажіть вік: "))
        except ValueError:
            print("Введіть число!")
            continue
        address = input("Вкажіть адресу проживання: ")

        if not name or not address:
            print("Поле не може бути пустим")
            continue

        if address.strip().isdigit():
            print("Адреса не може складатись тільки з цифр!")
            continue
        
        if len(address.strip()) < 5:
            print("Адреса занадто коротка")
            continue

        users[name] = {
            'age':age,
            'address':address
        }
        rewrite_file(users)
        print("Користувача додано")

    elif choice == "2":
        users = load_info()

        if not users:
            print("Інформація відсутня.")
            continue

        names = list(users.keys())

        for i, name in enumerate(names, 1):
            print(f"{i}. {name}")

        try:
            index = int(input("Введіть користувача: "))
            name = names[index - 1]
        except (ValueError, IndexError):
            print("Невірний вибір")
            continue

        key = input("Введіть назву поля (наприклад середній бал): ")

        value = input("Вкажіть значення поля: ")
        try:
            value = float(value)
            if value.is_integer():
                value = int(value)
        except:
            pass

        if key in users[name]:
            answer = input("Данне поле вже присутнє.Перезаписати? (так/ні): ")
            if answer.lower() != "так":
                print("Операцію скасовано")
                continue

        users[name][key] = value
        rewrite_file(users)

        print("Інформацію додано")

    elif choice == "3":
        users = load_info()

        if not users:
            print("Інформація відсутня")
            continue

        names = list(users.keys())

        for i ,name in enumerate(names, 1):
            print(f"{i}. {name}")

        try:
            index = int(input("Введіть користувача: "))

            if index < 1 or index > len(names):
                print("Невірний вибір")
                continue
            
            name = names[index - 1]
        except (ValueError, IndexError):
            print("Невірний вибір")
            continue
        
        print(f"Редагуєш данні користувача: {name}")

        fields = list(users[name].keys())

        for i, k in enumerate(fields, 1):
            print(f"{i}. {k}: {users[name][k]}")
        try:
            index = int(input("Виберіть поле"))
            key = fields[index - 1]
        except (ValueError, IndexError):
            print("Невірний вибір!")
            continue
        
        value = input("Введіть нове значення: ")

        try:
            value = float(value)
            if value.is_integer():
                value = int(value)
        except ValueError:
            pass

        users[name][key] = value
        rewrite_file(users)

        print("Данні оновлено")

    elif choice == "4":
        users = load_info()

        if not users:
            print("Інформація відсутня")
            continue

        names = list(users.keys())

        for i ,name in enumerate(names, 1):
            print(f"{i}. {name}")

        print("\n1.Переглянути одного користувача")
        print("2.Переглянути всіх користувачів")

        sub_choice = input("Оберіть дію: ")

        if sub_choice == "1":
            try:
                index = int(input("Введіть користувача: "))
                name = names[index - 1]
            except (ValueError, IndexError):
                print("Невірний вибір")
                continue

            data = users[name]
            info = " | ".join([f"{k}: {v}" for k,v in data.items()])

            print(f"\n{name}, {info}")

        elif sub_choice == "2":
            print("-----Всі користувачі:-----")
            for name, data in users.items():
                info = " | ".join([f"{k}: {v}" for k,v in data.items()])
                print(f"{name}, {info}")
        else:
            print("Невірний вибір")
            continue
        
    elif choice == "5":
        users = load_info()

        if not users:
            print("Інформація відсутня")
            continue

        print("\nСписок користувачів:")
        names = list(users.keys())

        for i, name in enumerate(names, 1):
            print(f"{i}. {name}")

        print("\n1.Видалити 1 користувача")
        print("2.Видалити всіх користувача")

        sub_choice = input("Виберіть дію: ")

        if sub_choice == "1":
            try:
                index = int(input("Виберіть користувача, щоб видалити: ")) - 1

                if index < 0 or index >= len(names):
                    print("Невірний вибір")
                    continue

                name = names[index]
            except (ValueError, IndexError):
                print("Невірний вибір")
                continue

            confirm = input(f"Підтвердити видалення {name}? (так/ні):")
            if confirm.lower() != "так":
                print("Операцію скасовано")
                continue

            del users[name]
            print(f"Користувача {name} успішно видалено")
            rewrite_file(users)

        elif sub_choice == "2":
            answer = input("Ви впевнені? (так або ні): ")
            if answer.lower() == "так":
                users.clear()
                rewrite_file(users)
                print("Всіх користувачів видалено")
            else:
                print("Операцію скасовано")

    elif choice == "6":
        print("Дякую за користування")
        break
