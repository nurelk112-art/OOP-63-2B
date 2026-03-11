import random


class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} атакует!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает и восстанавливает здоровье")


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print("Воин атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print("Маг кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print("Ассасин атакует исподтишка!")


# создаём героев
warrior1 = Warrior("Aragorn", 10, 100, 50, 80)
mage1 = Mage("Saruman", 9, 80, 40, 100)
assassin1 = Assassin("Nemo", 8, 90, 45, 95)

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



# Mини игра
print("Выберите героя:")
print("1 - Warrior")
print("2 - Mage")
print("3 - Assassin")

choice = input("Ваш выбор: ")

if choice == "1":
    player = warrior1
elif choice == "2":
    player = mage1
elif choice == "3":
    player = assassin1
else:
    print("Неверный выбор")
    exit()


# противник выбирается случайно
heroes = [warrior1, mage1, assassin1]
enemy = random.choice(heroes)

print("\nВы выбрали:", type(player).__name__)
print("Противник:", type(enemy).__name__)


# логика победителя
if type(player) == type(enemy):
    print("Ничья!")

elif isinstance(player, Warrior) and isinstance(enemy, Assassin):
    print("Warrior победил!")

elif isinstance(player, Assassin) and isinstance(enemy, Mage):
    print("Assassin победил!")

elif isinstance(player, Mage) and isinstance(enemy, Warrior):
    print("Mage победил!")

else:
    print(f"{type(enemy).__name__} победил!")

