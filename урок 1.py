class Dog:
    def __init__(self, name: object, age: object) -> None:
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} Гав!")
        dog1 = Dog("Sharik", 3)
        dog1.bark()