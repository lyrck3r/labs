import os
import json

categories = []

if os.path.exists('categories.txt'):
    with open('categories.txt', 'r', encoding='utf-8') as file:
        categories = [line.strip() for line in file]

def save_spendings(spendings):
    with open("spendings.json", "w") as f:
        json.dump(spendings, f, ensure_ascii=False, indent=4)

def load_spendings():
    try:
        with open("spendings.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return[]

spendings = load_spendings()

def save_balance(balance):
    with open("balance.txt", "w") as file:
        file.write(str(balance))

def load_balance():
    try:
        with open("balance.txt", "r") as file:
            return float(file.read())
    except FileNotFoundError:
        return 0.0

def no_category():
    print("Категорії не існую.Створіть її.")
    new_cat = input("Назва категорії: ").strip()
    if not new_cat:
            print("Назва не може бути пустою.")
            return None
    
    categories.append(new_cat)
    
    with open("categories.txt", 'a', encoding='utf-8') as file:
        file.write(new_cat + '\n')

    print("Категорію успішно додано")
    return new_cat

while True:
    print("\n========Меню========")
    print("1.Додати кошти")
    print("2.Додати витрату")
    print("3.Додати категорію")
    print("4.Баланс")
    print("5.Витрати")
    print("6.Сума витрат")
    print("7.Видалити категорію")
    print("8.Витрати по категоріях")
    print("9.Завершення роботи")

    choice = input("\nВиберіть операцію: ")

    if choice == "1":
        try:
            amount = float(input("Введіть суму для зарахування: "))
        except ValueError:
            print("Введіть число!")
            continue
        if amount <= 0:
            print("Сума має бути більше 0.")
        else:
            balance = load_balance()
            balance += amount
            save_balance(balance)
            print(f"Суму успішно зараховано. Ваш баланс: {balance} грн.")
    
    if choice == "2":
        name = input("Що купив? (або 'стоп'): ")
        balance = load_balance()
        if name.lower() == "стоп":
            continue
        try:
            amount = float(input("Скільки витратив?: "))
        except ValueError:
            print ("Введіть число!")
            continue
        
        category = input("Введіть категорію: ")
        if category not in categories:
            category = no_category()
            if category is None:
                continue

        if balance < amount:
            print("Недостатньо коштів")
            continue

        else:
            balance -= amount
            save_balance(balance)
            spendings.append({
                "name":name,
                "spend":amount,
                "category":category
            })
        save_spendings(spendings)
        print(f"Витрата успішно додана. Ваш баланс: {balance} грн.")

    if choice == "3":
        new_cat = input("Введіть назву категорії (або 'стоп' для завершення): ")
        
        if new_cat.lower() == "стоп":
            continue
        
        if new_cat in categories:
            print("Така категорія вже існує")
            continue
    
        else:
            with open("categories.txt", 'a', encoding='utf-8') as file:
                file.write(new_cat.strip() + "\n")

            categories.append(new_cat.strip())

            print("Категорію успішно створено")
            for i, cat in enumerate(categories,start = 1):
                print(f"{i}. {cat}")

    if choice == "4":
        balance = load_balance()
        print(f"Ваш баланс: {balance} грн.")

    if choice == "5":
        spendings = load_spendings()

        if not spendings:
            print("Витрат немає.")
            continue

        for i, s in enumerate(spendings, 1):
            print(f"{i}. {s['name']} | {s['spend']} грн | {s['category']}")
        
    if choice == "6":
        spendings = load_spendings()
        total = sum(s["spend"] for s in spendings)
        print(f"\nЗагальна сума витрат = {total} грн")

    if choice == "7":
        if not categories:
            print("Список порожній")
            continue
        print("\nСписок категорій: ")

        for i, cat in enumerate(categories, start=1):
            print(f"{i}. {cat}")
        try:
            num = int(input("Введіть номер категорії для видалення: "))

            if 1 <= num <= len(categories):
                removed = categories.pop(num -1)
                print(f"Категорію {removed} видалено!")
                with open("categories.txt", "w", encoding="utf-8") as file:
                    for cat in categories:
                        file.write(cat + "\n")
            else:
                print("Невірний номер.")
        except ValueError:
            print("Введіть число!")

    if choice == "8":
        spendings = load_spendings()

        if not spendings:
            print("Витрат немає.")
            continue

        stats = {}

        for s in spendings:
            cat = s['category']
            amount = s['spend']

            if cat in stats:
                stats[cat] += amount
            else:
                stats[cat] = amount

        print("\nСтатистика по категоріям: ")

        for cat, total in stats.items():
            print(f"{cat}: {total} грн")

    if choice == "9":
        print("Дякую за використання!")
        break
