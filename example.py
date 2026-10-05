try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Помилка: Файл не знайдено!")
finally:
    file.close()
    print("Файл закрито.")