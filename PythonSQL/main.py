import mysql.connector

MyFirstDB = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'mytestdb'
)

def InsertTable(): # функція - де ми будемо додавати 
    name = input("Введіть ваше ім'я: ")
    address = input("Введіть вашу адресу: ")

    MyCursor = MyFirstDB.cursor()
    sql = "INSERT INTO infouser (name, address) VALUES (%s, %s)"
    val = (name, address)
    MyCursor.execute(sql, val)

    MyFirstDB.commit()

def DeleteUserInTable():
    name = input("Введіть ваше ім'я, щоб видалити: ")
    MyCursor = MyFirstDB.cursor()
    sql = f"DELETE FROM infouser WHERE name = '{name}'"

    MyCursor.execute(sql)

    MyFirstDB.commit()

def PrintTable():
    MyCursor = MyFirstDB.cursor()

    MyCursor.execute("SELECT * FROM infouser")

    text = MyCursor.fetchall()

    for i in text:
        print(i)

def PrintUser():
    MyCursor = MyFirstDB.cursor()

    name = input("Введіть ваше ім'я: ")

    sql = f"SELECT * FROM infouser WHERE name = '{name}'"

    MyCursor.execute(sql)
    text = MyCursor.fetchall()

    count = 0
    for i in text:
        print(i)
        count = 1
    
    if count == 0:
        print("Такого юзера немає!")

def main():
    num = int(input("Для того, щоб додати користувача, напишіть '1'\nДля того, щоб видалити напишіть '2'\n"
        + "Для того, щоб вивести всю БД, напишіть '3'\n"
        + "Для того, щоб вивести інформацію про людину, напишіть '4'\n"))
    if num == 1:
        InsertTable()
    elif num == 2:
        DeleteUserInTable()
    elif num == 3:
        PrintTable()
    elif num == 4:
        PrintUser()
    else:
        print("Помилка!")

main()
