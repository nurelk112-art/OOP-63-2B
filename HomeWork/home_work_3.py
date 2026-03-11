from abc import ABC, abstractmethod

# Абстрактный класс Hero
class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health  # приватный атрибут (инкапсуляция)
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        self.__health += 1
        print(f"{self.name} отдыхает. Здоровье увеличено на 1!")

    @abstractmethod
    def attack(self):
        pass  # абстрактный метод, обязательно реализуется в дочерних классах

# Дочерние классы с реализацией attack()
class Warrior(Hero):
    def attack(self):
        print("Воин атакует мечом!")

class Mage(Hero):
    def attack(self):
        print("Маг использует магию!")

class Assassin(Hero):
    def attack(self):
        print("Ассасин атакует из-под тишка!")

# Создание объектов
warrior1 = Warrior("Sauron", 10, 100, 50)
mage1 = Mage("Gendalf", 9, 80, 40)
assassin1 = Assassin("StormShadow", 8, 90, 45)

# Вызов методов каждого героя
print("----- Warrior -----")
warrior1.greet()
warrior1.attack()
warrior1.rest()

print("\n----- Mage -----")
mage1.greet()
mage1.attack()
mage1.rest()

print("\n----- Assassin -----")
assassin1.greet()
assassin1.attack()
assassin1.rest()