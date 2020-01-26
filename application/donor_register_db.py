#Imported libraries
import sqlite3
import bcrypt
import os

#Remove existing db
try:
    os.remove('sql.db')
except OSError as e:
    print("Couldn't remove the sile:", e.strerror)

#SQL connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

# Make table
#Donor DB

c.execute('''CREATE TABLE IF NOT EXISTS donor
            (id integer primary key, email text, username text, password text, confirm_password text, phone text, name text)''')

c.execute('''INSERT INTO donor (email, username, password, confirm_password, phone, name) VALUES (?, ?, ?, ?, ?, ?)''', ('email@email.com', 'username', 'pass', 'pass','615 111 6666','namefield'))

conn.commit()
