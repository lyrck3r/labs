balance = 0
while True:
    print("\n=====Меню=====")
    print("1.Перевірити баланс")
    print("2.Внести гроші")
    print("3.Зняти кошти")
    print("4.Вийти")

    choice = input("Оберіть дію: ")

    if choice == "1":
        print(f"Ваш баланс: {balance}")

    elif choice == "2":
        amount = float(input("Скільки внести?: "))
        if amount > 0:
            balance += amount
            print(f"Гроші успішно зараховано. Ваш баланс: {balance} грн")
        else:
            print("Сума має бути більше 0")
    elif choice == "3":
        amount = float(input("Скільки зняти?: "))
        if amount > balance:
            print("Недостатньо коштів")
        elif amount <= 0:
            print("Сума має бути більша 0")
        else:
            balance -= amount
            print(f"Заберіть гроші.Ваш баланс: ", balance, "грн")
    elif choice == "4":
        print("Дякую за користування")
        break
