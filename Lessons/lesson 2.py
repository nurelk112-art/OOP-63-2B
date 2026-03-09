# class Hero:
#
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
#     def action(self):
#         return f"{self.name} Base action"
#
# class MageHero(Hero):
#
#     def __init__(self, name, lvl, hp, mp):
#         super().__init__(name, lvl, hp)
#         self.mp = mp
#
#     def action(self):
#         return f"HP: {self.hp} NAME: {self.name}"
#
#     def cast_spell(self):
#         return f"{self.mp} cast spell {self.name}"
#
# kirito = Hero("Kirito", 100, 1000)
# asuna = MageHero("Asuna", 1000, 1000, 99)
#
# print(kirito.name)
# print(asuna.name)



class Step:
    def action(self):
        print('Step')

class Fly:
    def action(self):
        print('Fly')

class Swim:
    def action(self):
        print('Swim')

class Animal(Fly, Step, Swim):
    ...

duck = Animal()
# duck.action()
# print(Animal.mro())



class A:
    def action(self):
        print("A")
class B(A):
    def action(self):
        super().action()
        print("B")
class C(A):
    def action(self):
        super().action()
        print("C")
class D(B, C):
    def action(self):
        super().action()
        print("D")

test = D()
# test.action()
# print(D.mro())


    ### Practice ###

# class Vehicle:
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#
#     def move(self):
#         print("транспорт движется")
#
#
# class Car(Vehicle):
#     def move(self):
#         print("Машина едет")
#
# class Bike(Vehicle):
#     def move(self):
#         print("Велосипед едет")
#
#
# #создаём объекты
# car1 = Car("BMW", 220)
# bike1 = Bike("Trek",30)
#
# #вызываем методы
# car1.move()
# bike1.move()


   ###  Practice ###

# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Student(Person):
#
#     def __init__(self, name, age, university):
#         super().__init__(name, age)
#         self.university = university
#
#
# #создаём объект
# student1 = Student("nurel", 21, "KNU")
#
# #вызываем метод
# print(student1.name)
# print(student1.age)
# print(student1.university)
