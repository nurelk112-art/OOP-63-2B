class Car:
    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

    def description(self):
        return f"Машина: {self.name}, Возраст: {self.age}, Скорость: {self.speed}"

    def increase_speed(self):
        self.speed += 10
        return f"Новая скорость: {self.speed}"


# создаём 2 объекта
car1 = Car("BMW", 3, 120)
car2 = Car("Audi", 5, 100)

# вызываем методы
print(car1.description())
print(car1.increase_speed())

print(car2.description())
print(car2.increase_speed())