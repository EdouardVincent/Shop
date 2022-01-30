import sqlite3

conn = sqlite3.connect('my_database.sqlite')
cur = conn.cursor()

cur.execute ('''DROP TABLE IF EXISTS clients''')
cur.execute('''CREATE TABLE clients (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, email TEXT)''')
    
a=0
while True :
    nom_client = input("Nom (client) : ")
    email_client = input("email (client) : ")

    cur.execute('''INSERT INTO clients(name, email) VALUES (?,?)''',(nom_client, email_client))

    a+= 1

    conn.commit()


cur.close()

