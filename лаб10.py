"""
    Класс створення книги
    def __init__(self,name,publisher,year):
    __init__ - використовується для ініціалізації атрибутів об'єктів
    self - обов'язково всюди
    name, publisher, year - поля класу

    def __str__(self):  - повертає рядок,що описує об'єкт
    return - повертає опис об'єкта
"""
class Book:
    def __init__(self, name, publisher, year):
        self.name = name
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return (f"Назва книги - {self.name}. Автор - {self.publisher}. Рік видавництва - {self.year}")

"""
    Цикл опису книги, як об'єкту

    if any(char.isdigit() for char in name|publisher): - перевірка, щооб не було цифр в значенні полів "name"|"surname"
    Продовження програми поки не буде введений правильне значення

    try: - обробка вийнятків
    except ValueError: - вийняток введення не числа
"""
while True:
    # Введення інформації від користувача
    name = input("Введіть назву книгі: ")
    if any(char.isdigit() for char in name):
        print("Не можна вводити цифри")
        continue
    # Введення інформації від користувача
    publisher = input("Введіть автора книгі: ")
    if any(char.isdigit() for char in publisher):
        print("Не можна вводити цифри")
        continue
    try:
        # Введення інформації від користувача
        year = int(input("Введіть рік видання книгі: "))
    except ValueError:
        print("Введіть число!")
        continue
    # Виведення об'єкту "Книга" і завершення програми
    book = Book(name, publisher, year)
    print(book)
    break

"""
    Клас студент
    def __init__(self, name, surname, score):
    __init__ - використовується для ініціалізації атрибутів об'єктів
    self - обов'язково всюди
    name, surname, score - поля класу

    def score_level(self): - метод вичеслення рівня знань студента
    - if self.score <33: - якщо оцінка нижче 33
    return "Низький" - повертає значення "Низький"
    - elif self.score <= 66: - якщо оцінка нижче-рівне 66
    return "Середній" - поверає значення "Середній
    - else: - остальні значення оцінки
    return "Високий" - повертає значення "Високий"

    def __str__(self):  - повертає рядок,що описує об'єкт
    return - повертає опис об'єкта
"""
class Student:
    def __init__(self, name, surname, score):
        self.name = name
        self.surname = surname
        self.score = score

    def score_level(self):
        if self.score <33:
            return "Низький"
        elif self.score <= 66:
            return "Середній"
        else:
            return "Високий"

    def __str__(self):
        return (f"Ім'я - {self.name}. Прізвище - {self.surname}. Рівень знань - {self.score_level()}")

"""
    Цикл опису студента, як об'єкт

    if any(char.isdigit() for char in name): - перевірка чи є в значенні поля "name" цифри
    if any(char.isdigit() for char in surname): - перевірка чи є в значенні поля "surname" цифри
    Будуть працювати, поки не буде введено коректне значення

    try: - обробка вийнятків
    except ValueError: - вийняток введення не числа
"""
while True:
    # Введення інформації користувачем
    name = input("Введіть ім'я: ").capitalize()
    if name.isdigit():
        print("Не можна вводити цифри")
        continue
    # Введення інформації користувачем
    surname = input("Введіть прізвище: ").capitalize()
    if surname.isdigit():
        print("Не можна вводити цифри")
        continue
    try:
        # Введення інформації користувачем
        score = int(input("Введіть бал: "))
    except ValueError:
        print("Введіть число!")
        continue

    # Виведення інформації про студента і завершення програми
    student = Student(name, surname, score)
    print(student)
    break

"""
    Клас створення прямокутника
    def __init__(self, width, lenght):
    __init__ - використовується для ініціалізації атрибутів об'єктів
    self - обов'язково всюди
    width, lenght - назви полів

    def __str__(self): - метод повернення рядку, що описує об'єкт
    return () - повертає інформацію про об'єкт

    def calculation_area(self): - метод обчислення площі прямокутника
    area = self.width * self.lenght - поле обчислення площі
    return - повернення поля

    def calculation_perimeter(self): - метод обчислення периметру прямокутника
    perimeter = 2 * (self.lenght + self.width) - поле обчислення периметру
    return perimeter - повернення поля
"""
class Rectangle:
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght

    def __str__(self):
        return (f"Довжина прямокутника - {self.lenght}.\n"
                f"Ширина прямокутника - {self.width}.\n"
                f"Площа прямокутника - {self.calculation_area()}.\n"
                f"Перемитер прямокутника - {self.calculation_perimeter()}")
    
    def calculation_area(self):
        area = self.width * self.lenght
        return area

    def calculation_perimeter(self):
        perimeter = 2 * (self.lenght + self.width)
        return perimeter

"""
    Цикл опису прямокутника, як об'єкта

    try: - обчислення вийнятків
    except ValueError: - вийняток введення не числа
"""
while True:
    try:
        # Введення данних користувачем
        lenght = int(input("Введіть довжину сторони прямокутника: "))
        width = int(input("Введіть ширину сторони прямокутника: "))
    except ValueError:
        print("Введіть число!")
        continue
    
    # Виведення інформації про прямокутник і завершення програми
    rectangle = Rectangle(lenght, width)
    print(rectangle)
    break