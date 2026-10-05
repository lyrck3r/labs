# Імпортуємо з модуля "module1" функцію "greet"
from module1 import greet as hi

# Виведення привітання команди
def greet_team(names):
    for name in names:
        print(hi(name))

# Виведення повідомлення на екран
if __name__ == "__main__":
    team = ["Анна", "Влад", "Михайло", "Світлана"]
    greet_team(team)