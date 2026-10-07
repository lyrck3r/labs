from database import Database
from expense_manager import ExpenseManager


def show_menu():
    print("\n==================================")
    print("        Калькулятор витрат")
    print("\n==================================")
    print("1.Додати витрату")
    print("2.Показати всі витрати")
    print("3.Видалити витрату")
    print("4.Показати загальну суму")
    print("0. Вийти")
    print("==================================")


def main():
    database = Database()
    manager = ExpenseManager(database)

    while True:
        show_menu()

        choice = input("Виберіть дію: ")

        if choice == "1":
            name = input("Назва витрати: ")

            amount = float(
                input("Сума: ")
            )

            category = input("Категорія: ")

            expense_date = input("Дата (YYYY-MM-DD):")

            manager.add_expense(
                name,
                amount,
                category,
                expense_date
            )

            print("Витрату успішно додано!")

        elif choice == "2":
            manager.show_expenses()

        elif choice == "3":
            manager.show_expenses()

            expense_id = int(
                input("ID витрати для видалення: ")
            )

            manager.delete_expense(expense_id)

            print("Витрату успішно видалено!")

        elif choice == "4":
            total = manager.get_total()

            print(
                f"\nЗагальна сума витрат {total} грн"
            )

        elif choice == "0":
            database.close()

            print("Програму завершено!")
            break
        else:
            print("\nНевірний вибір!")

if __name__ == "__main__":
    main()