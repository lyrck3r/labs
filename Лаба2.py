# 2.2.1. Оголосити змінні різних типів
age = 23  # Ціле число
name = "Влад"  # Рядок
is_student = True  # Логічна умова
grades = [67, 83, 90]  # Список

# Перевірка змінних і виведення результатів
print("Результат: ", age, " | Тип: ", type(age))
print("Результат: ", name, " | Тип: ", type(name))
print("Результат: ", is_student, " | Тип: ", type(is_student))
print("Результат: ", grades, " | Тип: ", type(grades))

# 2.2.2. Реалізувати умовну конструкцію if-else
number = int(input("Введіть ціле число: "))
if number > 0:
    print("Число додатнє.")
else:
    if number == 0:
        print("Число дорівнює нулю.")
    else:
        print("Число від\'ємне")

# 2.2.3. Використати цикл for
number = int(input("Введіть ціле число: "))
print("Таблиця множення для ", number, ":")
for i in range(1, 11):
    result = number * i
    print("Число ", number, "= " f"{number} x {i} = {result}")

# 2.2.4. Реалізувати цикл while з break
total = 0  # Початкова сума
while True:
    number = int(input("Введіть число (0 для завершення): "))
    total += number  # функція додавання

    if number == 0:
        break

print("Сума введених: ", total)
