import os
print("ПАПКА ЗАПУСКУ:", os.getcwd())

os.makedirs('data', exist_ok=True)
balance = 0
spendings = []
categories = []

if os.path.exists('data/categories.txt'):
    with open('data/categories.txt', 'r', encoding='utf-8') as file:
        categories = [line.strip() for line in file]

while True:
    print("=========Меню=========")
    print("1.Додати витрату")
    print("2.Додати кошти")
    print("3.Додати категорію")
    print("4.Переглянути витрати")
    print("5.Переглянути баланс")
    print("6.Видалити категорію")
    print("7.Завершити програму")

    choice = input("Виберіть дію: ")

    if choice == '1':
        name = input("Введіть назву витрати: (або стоп для завершення)")
        amount = float(input("Введіть суму витрати: "))

        if name.lower() == "стоп":
            break

        if amount <= 0:
            print("Сума має бути більшою за 0")
            continue

        category = input("Введіть категорію витрат: ")
        if category not in categories:
            print("Цієї категорії не існує.Спочатку створіть її.")
            new_cat = input("Назва категорії: ")
            categories.append(new_cat)
            category = new_cat
            print("Категорію додано")

        if amount > balance:
            print("Недостатньо коштів.")
        else:
            balance -= amount
            spendings.append({
                "name":name,
                "amount":amount,
                "category":category
            })
            print(f"Витрата успішно додана.Ваш баланс: {balance}")

    if choice == "2":
        amount = float(input("Скільки внести?: "))
        if amount > 0:
            balance += amount
            print(f"Гроші успішно зараховано. Ваш баланс: {balance} грн")
        else:
            print("Сума має бути більше 0")

    if choice == '3':
        name = input("Введіть назву категорії (або стоп для завершення): ")

        if name.lower() == "стоп":
            break
        else:
            path = os.path.join(os.getcwd(), "data", "categories.txt")

            with open(path, 'a', encoding='utf-8') as file:
                file.write(name.strip() + "\n")

            categories.append(name.strip())  # 🔥 ОЦЕ ВАЖЛИВО

            print("Категорію успішно створено!")

            print("\nСписок категорій:")
            for i, cat in enumerate(categories, start=1):
                print(f"{i}. {cat}")

    if choice == "4":
        print(f"Ваші витрати: {spendings}")

    if choice == "5":
        print(f"Ваш баланс: {balance}")
    
    if choice == '6':
        if not categories:
            print("Список категорій порожній.")
            continue

        print("\nСписок категорій:")
        for i, cat in enumerate(categories, start=1):
            print(f"{i}. {cat}")

        try:
            num = int(input("Введіть номер категорії для видалення: "))

            if 1 <= num <= len(categories):
                removed = categories.pop(num - 1)
                print(f"Категорію '{removed}' видалено!")

            # 🔥 перезапис файлу
                with open('data/categories.txt', 'w', encoding='utf-8') as file:
                    for cat in categories:
                        file.write(cat + "\n")

            else:
                print("Невірний номер.")

        except ValueError:
            print("Введіть число.")

    if choice == '7':
        print("Дякуємо за роботу.")
        break