import random
class BankAccount:

    def __init__(self, login, password, balance):
        self.login = login
        self._balance = balance
        self.__password = password

    def get_balance(self, password):
        if password == self.__password:
            return self._balance
        return "Неверный пароль!!"

    def __ganarete_pass(self):
        return random.randint(1, 6)

    def change_pass(self, old_pass, new_pass):
        if self.__password == old_pass:
            self.__password = self.__ganarete_pass()
            return "Пароль изменен!!"
        return "Неверный старый пароль!!"


# ardager = BankAccount('ardager', "Def2638", 1000)
#
# print(ardager._BankAccount__password)
# print(ardager.change_pass("Def2638", "123321"))
# # print(dir(ardager))
# print(ardager._BankAccount__password)






from abc import ABC, abstractmethod
#
# # Абстрактный класс
# class Animal(ABC):
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Dog(Animal):
#
#     def make_sound(self):
#         return  "Gaf Gaf"
#
#     def move(self):
#         return "Step Step"
#
# class Duck(Animal):
#
#     def move(self):
#         return "Step Step"
#
#     def make_sound(self):
#         return "Krya Krya!!"
#
#
# gufi = Dog()
#
# print(gufi.move())
# print(gufi.make_sound())



class OTPSend(ABC):

    @abstractmethod
    def send_otp_to_phone(self, phone):
        pass


class KGOTPSend(OTPSend):

    def send_otp_to_phone(self, phone):
        sms = """
            <Phone>+996779280699</Phone>
            <Text>Ваш пароль 1234</Text>
        """
        return sms

class RUOTPSend(OTPSend):

    def send_otp_to_phone(self, phone):
        sms = {
            "Phone": "+79652107311",
            "Text": "Ваш пароль 1234"
        }
        return sms
