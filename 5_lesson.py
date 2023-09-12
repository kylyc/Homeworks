import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    frist_name TEXT,
    last_name TEXT,
    age INTEGER
    )''')
# first_name = input("Введите имя")
# last_name = input("Введите фамилию")
# age = input("Введите возраст")

# cursor.execute("INSERT INTO users(first_name, last_name, age) VALUES ('{first_name}','{flast_name}', {age})")


# connect.commit()

# connect.close()

cursor.execute("""SELECT * FROM users""")

data = cursor.fetchall()

for result in data:
    print(f"ID: {result[0]}")
    print(f"")