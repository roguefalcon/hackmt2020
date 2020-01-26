#!/usr/bin/python3

# Imported libraries
import sqlite3
import bcrypt
import os

# We want to remove the existing file
try:
    os.remove('sql.db')
except OSError as e:
    print("Couldn't remove the file:", e.strerror)

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

# Make the tables =============================================================
#Children DB
c.execute('''CREATE TABLE IF NOT EXISTS children
             (id integer primary key, email text, name text, age  integer, about_me text, address text, cloth_size text, sex text, gender text, pant_size text, shoes_size text, fav_color text)''')

#Children_items
c.execute('''CREATE TABLE IF NOT EXISTS children_items
            (id integer primary key, name text, amount integer,children_id integer not null, foreign key (children_id) references children(id))''')

#Donor
c.execute('''CREATE TABLE IF NOT EXISTS donor
            (id integer primary key, email text, username text, password text, confirm_password text, phone text, name text)''')


#Load into donor
c.execute('''INSERT INTO donor (email, username, password, confirm_password, phone, name) VALUES (?, ?, ?, ?, ?, ?)''', ('email@email.com', 'username', 'pass', 'pass','615 111 6666','namefield'))
# Let's load some data
#c.execute('''INSERT INTO users VALUES (?, ?)''',
#         ('asdf', bcrypt.hashpw(b'asdf', bcrypt.gensalt())))
c.execute('''INSERT INTO children (email, name, age, about_me, address, cloth_size, sex, gender, pant_size, shoes_size, fav_color) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
          ('example@example.ea', 'NAME', 10, 'ABOUT ME INFORMATION', 'ADRESS LINE', 'SMALL', 'Male', 'M', 'S', '5', 'YELLOW'))

c.executemany('''INSERT INTO children_items (name, amount, children_id) VALUES(?, ?, ?)''',
          [('LEGO', 20, 1),('GIFT', 50, 1),('CANDY', 5, 1)])


conn.commit()
