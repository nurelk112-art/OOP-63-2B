from abc import ABC, abstractmethod
import random

class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name}, готов к бою!")

class MageHero(Hero):

    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        print(f"Maг {self.name} кастует заклинание! MP: {self.mp} ")

class Warrior(MageHero):

    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl} ")

    #Банк аккаунт
class BankAccount:
    bank_name = "Золотой банк Смауга"

    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance    #Защищённый атрибут
        self.__password = password #Приватный атрибут

    #Проверка пароля
    def login(self, password):
        if password == self.__password:
            print("Вход выполнен")
            return True
        else:
            print("Неверный пароль")
            return False

    #Свойство только для чтения
    @property
    def full_info(self):
        return f"Герой: {self.hero.name}, Уровень: {self.hero.lvl}, Баланс:{self._balance} "

    #Метод возвращяет название банка
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    # Бонус за уровень
    def bonus_for_lvl(self):
        return self.hero.lvl * 10

    # --- МАГИЧЕСКИЕ МЕТОДЫ ---
    def __str__(self):
        return f"{self.hero.name}, | Баланс: {self._balance} SOM"

    #Сложение балансов
    def __add__(self, other):
        if type(self.hero) == type(other.hero):
          return self._balance + other._balance
        else:
          return ValueError("Нельзя складывать счёта разных классов героев")

    def __eq__(self, other):
         return self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl


    # АБСТРАКТНЫЙ СЕРВИС SMS
class SmsService(ABC):

    @abstractmethod
    def send_otp(self, phone):
        pass

class KGSms(SmsService):

    def send_otp(self, phone):
        code = random.randint(1000, 9999)
        return f"<text>Код: {code}</text><phone>{phone}</phone>"


class RUSms(SmsService):

    def send_otp(self, phone):
        code = random.randint(1000, 9999)
        return {"text": f"Код: {code}", "phone": phone}


    # Герои
mage1 = MageHero("Gendalf", 80, 500, 150)
mage2 = MageHero("Saruman", 80, 500, 150)
warrior = Warrior("Aragorn", 50, 900, 20)


    #Банковские аккаунты
acc1 = BankAccount(mage1, 5000, "1234")
acc2 = BankAccount(mage2, 3000, "0000")
acc3 = BankAccount(warrior, 2500, "1111")

print("=== Действия героев ===")
mage1.action()
mage2.action()
warrior.action()

print("\n=== Банковские аккаунты ===")
print(acc1)
print(acc2)
print(acc3)

print("\n=== SMS сервис ===")
kg_sms = KGSms()
ru_sms = RUSms()
print(kg_sms.send_otp("+996555123456"))
print(ru_sms.send_otp("+79991234567"))

    # --- Классовые методы ---
print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_lvl(), "SOM")

    # --- __add__ ---
print("\n=== Проверка __add__ ===")

print("Сумма счетов двух магов:", acc1 + acc2)

try:
    print("Сумма мага и воина:", acc1 + acc3)
except ValueError as e:
    print(e)

    # --- __eq__ ---
print("\n=== Проверка __eq__ ===")

print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)

    # --- SMS ---
sms = KGSms()
print("\n", sms.send_otp("+996777123456"))