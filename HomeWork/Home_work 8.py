import sqlite3

# Создаём подключение к базе (файл создастся автоматически)
conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()

# -----------------------------
# ЧАСТЬ 1 — Создание таблиц
# -----------------------------
cursor.execute("DROP TABLE IF EXISTS reviews")
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("DROP TABLE IF EXISTS movies")

# Таблица пользователей
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

# Таблица фильмов
cursor.execute("""
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT
)
""")

# Таблица отзывов
cursor.execute("""
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
)
""")

# -----------------------------
# ЧАСТЬ 1 — Добавление данных
# -----------------------------
users = [
    (1, 'Alice'),
    (2, 'Bob'),
    (3, 'Charlie'),
    (4, 'Diana'),
    (5, 'Ethan')
]

movies = [
    (1, 'Inception', 'Sci-Fi'),
    (2, 'Titanic', 'Romance'),
    (3, 'Avengers', 'Action'),
    (4, 'Joker', 'Drama'),
    (5, 'Frozen', 'Animation')
]

reviews = [
    (1, 1, 1, 9),
    (2, 2, 1, 8),
    (3, 3, 2, 7),
    (4, 4, 2, 8),
    (5, 5, 3, 10),
    (6, 1, 3, 9),
    (7, 2, 4, 6),
    (8, 3, 4, 7),
    (9, 4, 5, 8),
    (10, 5, 5, 9)
]

cursor.executemany("INSERT INTO users VALUES (?, ?)", users)
cursor.executemany("INSERT INTO movies VALUES (?, ?, ?)", movies)
cursor.executemany("INSERT INTO reviews VALUES (?, ?, ?, ?)", reviews)
conn.commit()

# -----------------------------
# ЧАСТЬ 2 — JOIN
# -----------------------------
print("\nИмя пользователя + фильм + оценка:")
cursor.execute("""
SELECT u.name, m.title, r.rating
FROM reviews r
JOIN users u ON r.user_id = u.id
JOIN movies m ON r.movie_id = m.id
""")
for row in cursor.fetchall():
    print(row)

print("\nВсе фильмы (даже без отзывов):")
cursor.execute("""
SELECT m.title, r.rating
FROM movies m
LEFT JOIN reviews r ON m.id = r.movie_id
""")
for row in cursor.fetchall():
    print(row)

# -----------------------------
# ЧАСТЬ 3 — АГРЕГАЦИИ
# -----------------------------
cursor.execute("SELECT AVG(rating) FROM reviews")
avg_rating = cursor.fetchone()[0]

cursor.execute("SELECT MAX(rating) FROM reviews")
max_rating = cursor.fetchone()[0]

cursor.execute("SELECT MIN(rating) FROM reviews")
min_rating = cursor.fetchone()[0]

print("\nАгрегации по оценкам фильмов:")
print(f"Средняя оценка: {avg_rating:.2f}")
print(f"Максимальная оценка: {max_rating}")
print(f"Минимальная оценка: {min_rating}")

# Закрываем соединение
conn.close()