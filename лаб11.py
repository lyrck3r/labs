# Імпорт модулів
import random as rnd
import tkinter as tk
from datetime import date, datetime

"""
    Цикл генерації випадкового числа

    tru: - обробка виключень
    except ValueError - виведення виключення не введення числа

    random_nums = rnd.randint(num1, num2) - змінна, яка генерує випадкове числа в діапазоні чисел від "num1" до "num2"
"""
while True:
    try:
        # Введення данних користувачем
        num1 = int(input("Введіть перше число діапазону: "))
        num2 = int(input("Введіть друге число діапазону: "))
    except ValueError:
        print("Введіть число!")

    random_nums = rnd.randint(num1, num2)
    # Виведення інформації і завершення роботи
    print(f"Твоє випадкове число в діапазоні від {num1} до {num2} - {random_nums}.")
    break


"""
    Цикл обчислення віку і наступного дня народження

    today = date.today() - змінна, яка визначає сьогоднішю дату(!)

    try: - обробка виключень
    parsed_date = datetime.strptime(birthday, "%d.%m.%Y")
    - parsed_date - назва змінної
    - datetime.strptime - форматування рядка в дату
    - birthday - зміна, де користувач вводив свої данні
    - "%d.%m.%Y - формат дати
    except Value: - виведення виключення не введення числа

    if birthday_this_year < today: - умова, якщо "birthday_this_year" < today
    birthday_next = date(today.year + 1, parsed_date.month, parsed_date.day)
    Якщо день народження вже минув цього року, беремо наступний рік

    age = today.year - parsed_date.year - змінна обчислення років
    if (today.month, today.day) < (parsed_date.month, parsed_date.day):
    Умова перевірки дат для визначення віку
"""
while True:
    today = date.today()
    # Введеня інформації користувачем
    birthday = input("Введіть дату народження (dd.mm.yyyy): ")
    try:
        parsed_date = datetime.strptime(birthday, "%d.%m.%Y")
    except ValueError:
        print("Неправильний формат. Спробуйте ще раз")
        continue
    
    # Розбір дати народження цього року
    birthday_this_year = date(today.year, parsed_date.month, parsed_date.day)

    if birthday_this_year < today:
        birthday_next = date(today.year + 1, parsed_date.month, parsed_date.day)
    else:
        birthday_next = birthday_this_year

    # Визначення к-сті днів до наступного дня народження
    till_birthday = birthday_next - today
    # Виведення інформації
    print(f"До дня народження залишилось: {till_birthday.days} днів")

    age = today.year - parsed_date.year
    if (today.month, today.day) < (parsed_date.month, parsed_date.day):
        age -= 1
    # Виведення інформації
    print(f"Тобі {age} років")
    # Завершення роботи
    break

# Список цитат
advices = ['Найкраща помста — величезний успіх. Френк Сінатра',
            'Прагніть не до успіху, а до цінностей, які він дає. Альберт Айнштайн',
            'Життя — це те, що з тобою відбувається, поки ти будуєш плани. Джон Леннон',
            'Талант — це дар, якому неможливо ні навчити, ні навчитися. Іммануїл Кант']
# Список порад
quotes = ['Відмовтеся від сигарет і алкоголю.',
         'Щодня з\'їдайте по кілька свіжих фруктів або овочів.',
         'Думайте позитивно.','Робіть ранкову зарядку.']

# Фунція отримання поради
def get_advice():
    lable.config(text = rnd.choice(advices))

# Функція отримання цитати
def get_quote():
    lable.config(text = rnd.choice(quotes))

# Створення головного вікна
root = tk.Tk()
root.title("Моє перше GUI")

# Додавання тексту
lable = tk.Label(root, text = "Привіт користувач!")
lable.pack()

# Додавання кнопки, що отримати пораду
button1 = tk.Button(root, text = "Натисни, щоб отримати пораду", command=get_advice)
button1.pack()

# Додавання кнопки, що отримати цитати
button2 = tk.Button(root, text = "Натисни, щоб отримати цитату", command=get_quote)
button2.pack()

# Запуск головного циклу програми
root.mainloop()