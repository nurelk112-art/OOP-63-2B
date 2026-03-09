from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, lvl, health, strength):
        self.name = name
        self.lvl = lvl
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.lvl}")

    def rest(self):
        print(f"{self.name}, отдыхает...")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print("Воин атакует мечом!")


class Mage(Hero):
    def attack(self):
        print("Маг атакует магией!")


class Assassin(Hero):
    def attack(self):
        print("Ассасин атакует исподтишка!")


#создаём объекты
warrior1 = Warrior("Sauron", 99, 1000, 400)
mage1 = Mage("Gendalf", 75, 800, 200 )
assassin1 = Assassin("Tauriel", 70, 750, 300 )


#вызываем методы
print("=========== ВОИН ===========")
warrior1.greet()
warrior1.rest()
warrior1.attack()

print("\n=========== МАГ ===========")
mage1.greet()
mage1.rest()
mage1.attack()

print("\n========= АССАСИН =========")
assassin1.greet()
assassin1.rest()
assassin1.attack()