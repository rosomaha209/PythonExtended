import sqlite3

# Створення та підключення до бази даних
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Створення таблиці
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Перевірка наявності записів у таблиці
cursor.execute('SELECT COUNT(*) FROM users')
record_count = cursor.fetchone()[0]

if record_count == 0:
    # Додавання прикладів записів
    cursor.executemany('''
    INSERT INTO users (name, age)
    VALUES (?, ?)
    ''', [
        ('Michael', 25),
        ('Steve', 20),
        ('Lisa', 30),
        ('Tim', 44)
    ])

# Збереження змін та закриття з'єднання
conn.commit()
conn.close()

print("Database and table created with example records.")


def get_all_records():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()

    print("All Records:")
    for row in records:
        print(row)

    conn.close()


def get_records_in_range(min_value, max_value):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE age BETWEEN ? AND ?"
    cursor.execute(query, (min_value, max_value))
    records = cursor.fetchall()

    print(f"Records with age between {min_value} and {max_value}:")
    for row in records:
        print(row)

    conn.close()


def update_record(record_id, new_name, new_age):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Отримання поточних значень
    cursor.execute("SELECT name, age FROM users WHERE id = ?", (record_id,))
    record = cursor.fetchone()
    if not record:
        print(f"No record found with ID {record_id}")
        conn.close()
        return

    current_name, current_age = record

    # Встановлення нових значень або збереження старих, якщо нові не вказані
    updated_name = new_name if new_name else current_name
    updated_age = new_age if new_age else current_age

    query = "UPDATE users SET name = ?, age = ? WHERE id = ?"
    cursor.execute(query, (updated_name, updated_age, record_id))
    conn.commit()

    print(f"Record with ID {record_id} updated to name: {updated_name}, age: {updated_age}")

    conn.close()


def main():
    while True:
        print("\nMenu:")
        print("1. View all records")
        print("2. Search records by range")
        print("3. Update a record")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            get_all_records()
        elif choice == '2':
            min_value = int(input("Enter minimum age: "))
            max_value = int(input("Enter maximum age: "))
            get_records_in_range(min_value, max_value)
        elif choice == '3':
            record_id = int(input("Enter the ID of the record to update: "))
            new_name = input("Enter the new name (leave blank to keep current): ")
            new_age = input("Enter the new age (leave blank to keep current): ")
            new_age = int(new_age) if new_age else None
            update_record(record_id, new_name, new_age)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
