import sqlite3

# Подключение к базе данных (создаст файл если его нет)
conn = sqlite3.connect("store.db")
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    quantity INTEGER
)
""")
conn.commit()


# ---------------- CREATE ----------------
def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    conn.commit()
    print("Товар добавлен!")


# ---------------- READ ----------------
def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    print("\nСписок товаров:")
    for product in products:
        print(product)


# ---------------- UPDATE ----------------
def update_product(id, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, id)
    )
    conn.commit()
    print("Цена обновлена!")


# ---------------- DELETE ----------------
def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (id,)
    )
    conn.commit()
    print("Товар удалён!")


# ---------------- Проверка ----------------
if __name__ == "__main__":

    # CREATE
    create_product("iPhone", 800, 5)
    create_product("Samsung", 700, 3)

    # READ
    read_products()

    # UPDATE
    update_product(1, 850)

    # READ после обновления
    read_products()

    # DELETE
    delete_product(2)

    # READ после удаления
    read_products()

    conn.close()