import sqlite3

# A4
connect = sqlite3.connect("users.db")
# рука с ручкой
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (50) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()


#CRUD Create - Read - Update - Delete

def create_user(name, age, hobby):
    cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")')
    connect.commit()
    print('пользователь добавлен!!')

# create_user("Arzybek", 27, "Аниме-Манга-Манхва")

