import sqlite3;

connection = sqlite3.connect("PWA.db")

crsr = connection.cursor()

print("Connected to the database")

sql_command = """CREATE TABLE emp (
user_id INTEGER, 
title VARCHAR(50),
body (username) VARCHAR(50),
body (password) VARCHAR(30),
);"""

crsr.execute(sql_command)

# primary key
id = [1, 5, 7]

# Enter 3 individuals usernames
username = ['Liam Mackenzie-Smith', 'Phill Legge', 'Cy Jones']

# Enter 3 individuals passwords
password = ['Dressage7', '12345', '78910']

for i in range(5):

    # This is the q-mark style:
    crsr.execute(
    'INSERT INTO emp VALUES (?, ?, ?)'
    ('id[i], username[i], password[i]')
    )

crsr.execute("SELECT * FROM user_id")

ans = crsr.fetchall()

for i in ans:
    print(i)

connection.commit()

connection.close()





