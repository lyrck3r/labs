# Список чисел
nums = []

# Функція додавання
def function_plus(num1, num2):
    """
    Додає число num1 до num2
    
    Аргументи:
        num1 (float): доданок
        num2 (float): доданок

    Return:
        float: сума
    """
    return num1 + num2

# Функція віднімання
def function_minus(num1, num2):
    """
    Віднімає число num1 від num2
    
    Аргументи:
        num1 (float): зменшувальне
        num2 (float): від'ємник

    Return:
        float: різниця
    """
    return num1 - num2

# Функція множення
def function_multiply(num1, num2):
    """
    Множить число num1 на num2
    
    Аргументи:
        num1 (float): множник
        num2 (float): множник

    Return:
        float: добуток
    """
    return num1 * num2

# Функція ділення
def function_division(num1, num2):
    """
    Ділить число num1 на num2
    
    Аргументи:
        num1 (float): ділене
        num2 (float): дільник

    Return:
        float: частка

    Raises:
        ValueError: Якшо num2 дорівнює нулю.
    """
    if num2 == 0:
        raise ValueError("На нуль ділити заборонено")
    # повернення ділення чисел
    return num1 / num2

# Функція перевірки числа в списку
def no_nums():
    """
    Запитує у користувача два числа та повертає їх.

    Якщо введення некоректне (не число), обробляє помилку
    та повертає (None, None).

    Returns:
        tuple: Кортеж із двох чисел (float, float) або (None, None) у разі помилки.
    """
    try:
        print("Чисел не існує.Запишіть їх спочатку.")   # Виведення інформації про числа
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        # Додавання чисел в список
        return num1, num2
    except ValueError:                                  # Виведення помилки
        print("Введіть число!")
        return None, None                             

# Функція перевірки задання чисел
def ensure_nums(num1, num2):
    """
    Перевіряє, чи задані числа.

    Якщо хоча б одне значення дорівнює None, викликає функцію no_nums()
    для повторного введення чисел.

    Args:
        num1 (float | None): Перше число.
        num2 (float | None): Друге число.

    Returns:
        tuple: Кортеж із двох чисел (float, float).
    """
    if None in (num1, num2):
        num1, num2 = no_nums()
    return num1, num2

# Обов'язкове визначення чисел перед циклом
num1 = None
num2 = None

while True:
    print("1.Додати числа")
    print("2.Додавання")
    print("3.Віднімання")
    print("4.Множення")
    print("5.Ділення")
    print("6.Видалити числа")
    print("7.Переглянути числа")
    print("8.Переглянути рядки документації")
    print("9.Завершення програми")

    choice = input("\nВиберіть дію: \n")

    if choice == "1":
        try:
            num1 = float(input("Введіть перше число: "))    # додавання першго числа
            num2 = float(input("Введіть друге число: "))    # додавання другого числа  
        except ValueError:
            print("Введіть число!")                         # перевірна на правельність введення
            continue
        if (num1, num2) in zip(nums[::2], nums[1::2]):                   # перевірка чи є числа в списку
            print("Числа вже додані")
            continue
        print(f"Числа додані. Поточні числа: {num1}, {num2}")    # виведеня інформації про додавання чисел в список
        nums.append(num1)                               # додавання першго числа в список
        nums.append(num2)                               # додавання другого числа в список

    if choice == "2":
        # перевірка на наявність чисел
        num1, num2 = ensure_nums(num1, num2)
        if num1 is None or num2 is None:
            continue
        result = function_plus(num1, num2)
        print(f"Сума чисел = {result}")

    if choice == "3":
        # перевірка на наявність чисел
        num1, num2 = ensure_nums(num1, num2)
        if num1 is None or num2 is None:
            continue
        result = function_minus(num1, num2)
        print(f"Віднімання чисел = {result}")

    if choice == "4":
        # перевірка на наявність чисел
        num1, num2 = ensure_nums(num1, num2)
        if num1 is None or num2 is None:
            continue
        result = function_multiply(num1, num2)
        print(f"Множення чисел = {result}")

    if choice == "5":
        # перевірка на наявність чисел
        num1, num2 = ensure_nums(num1, num2)
        if num1 is None or num2 is None:
            continue
        try:   
            result = function_division(num1, num2)
            print(f"Ділення чисел = {result}")
        except ValueError as e:
            print(e)

    if choice == "6":
        # очистка списку
        nums.clear()
        num1 = None
        num2 = None
        print("Список чисел очищений")

    if choice == "7":
        # виведення списку чисел
        if not nums:
            print("Список порожній.")
        else:
            for i, num in enumerate(nums, 1):
                print(f"{i}. {num}")

    if choice == "8":
        # Вибір документації
        print("1.Функція додавання")
        print("2.Функція віднімання")
        print("3.Функція множення")
        print("4.Функція ділення")
        print("5.Функція перевірки чисел в списку")
        print("6.Функція перевірки задання чисел")

        choice = input("\nВиберіть документацію: ")
        # Функція додавання
        if choice == "1":
            print(function_plus.__doc__)
        # Функція віднімання
        elif choice == "2":
            print(function_minus.__doc__)
        # Функція множення            
        elif choice == "3":
            print(function_multiply.__doc__)
        # Функція ділення            
        elif choice == "4":
            print(function_division.__doc__)
        # Функція перевірки чисел в списку    
        elif choice == "5":
            print(no_nums.__doc__)
        # Функція перевірки задання чисел    
        elif choice == "6":
            print(ensure_nums.__doc__)

    if choice == "9":
        # завершення програми
        print("Дякую за користування.\n")
        break
    
    else:
        print("\nНевірний номер.\n")
        continue