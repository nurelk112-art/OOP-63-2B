# Задание 1
# Класс пользователя
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


# Декоратор проверки администратора
def is_admin(func):
    def wrapper(user):
        if user.role == "admin":
            return func(user)
        else:
            print("У вас нет доступа")
    return wrapper


# Функция удаления видео
@is_admin
def delete_video(user):
    print("Видео удалено")


# Проверка
admin = User("Ardager", "admin")
user = User("Bek", "user")

delete_video(admin)  #  Видео удалено
delete_video(user)   #  У вас нет доступа


# Задание 2
import time


# Декоратор таймера
def timer(func):
    def wrapper():
        start = time.time()

        func()

        end = time.time()
        print(f"Время выполнения: {round(end - start, 1)} секунд")

    return wrapper


# Функция загрузки видео
@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")


# Запуск
download_video()