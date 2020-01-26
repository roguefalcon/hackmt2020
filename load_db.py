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

#Donar_sponsor_children
c.execute('''CREATE TABLE IF NOT EXISTS donar_sponsor_children
            (id integer primary key, donar_id integer not null, children_id integer not null, foreign key (children_id) references children(id), foreign key (donar_id) references donar(id))''')


#Load into donor
c.execute('''INSERT INTO donor (email, username, password, confirm_password, phone, name) VALUES (?, ?, ?, ?, ?, ?)''', ('email@email.com', 'username', 'pass', 'pass','615 111 6666','namefield'))
# Let's load some data
#c.execute('''INSERT INTO users VALUES (?, ?)''',
#         ('asdf', bcrypt.hashpw(b'asdf', bcrypt.gensalt())))
#1
c.execute('''INSERT INTO children (email, name, age, about_me, address, cloth_size, sex, gender, pant_size, shoes_size, fav_color) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
          ('sammy@gmail', 'Sam', 6, 'I love kitties', '345 main street', 'SMALL', 'Female', 'F', 'S', '5', 'Pink'))
#2
c.execute('''INSERT INTO children (email, name, age, about_me, address, cloth_size, sex, gender, pant_size, shoes_size, fav_color) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
          ('KimmyMom@hotmail.com', 'Kim', 4, 'I just turned 4 and I like green', '786 GreenLand Drive', 'SMALL', 'Female', 'F', 'S', '3', 'Green'))
#3
c.execute('''INSERT INTO children (email, name, age, about_me, address, cloth_size, sex, gender, pant_size, shoes_size, fav_color) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
          ('DaJones@outlook.com', 'Sandy', 2, 'I like barbies', '912 RedWhite Drive', 'SMALL', 'Female', 'F', 'S', '2', 'Blue'))
#4
c.execute('''INSERT INTO children (email, name, age, about_me, address, cloth_size, sex, gender, pant_size, shoes_size, fav_color) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
          ('nikia@gmail.com', 'Olivia', 3, 'I just turned 3', '861 Freelance Street', 'SMALL', 'Female', 'F', 'S', '4', 'Pink'))
#5
c.execute('''INSERT INTO children (email, name, age, about_me, address, cloth_size, sex, gender, pant_size, shoes_size, fav_color) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
          ('Timmytim@gmail.com', 'Tim', 8, 'I play basketball a lot.', '861 Roxy Street', 'Medium', 'Male', 'M', 'S', '8', 'Purple'))
#6
c.execute('''INSERT INTO children (email, name, age, about_me, address, cloth_size, sex, gender, pant_size, shoes_size, fav_color) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
          ('Mandyt94@gmail.com', 'Mandy', 7, 'I enjoy reading books', '888 Newland Drive', 'Medium', 'Female', 'F', 'S', '4', 'Red'))
#7
c.execute('''INSERT INTO children (email, name, age, about_me, address, cloth_size, sex, gender, pant_size, shoes_size, fav_color) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
          ('AmandaMom@outlook.com', 'Amanda', 6, 'I enjoy to go shopping', '657 Seriance Street', 'SMALL', 'Female', 'F', 'S', '5', 'Purple'))        
#8
c.execute('''INSERT INTO children (email, name, age, about_me, address, cloth_size, sex, gender, pant_size, shoes_size, fav_color) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
          ('nikia@gmail.com', 'Olivia', 4, 'I am part of a band', '612 Freelance Street', 'SMALL', 'Female', 'F', 'S', '4', 'Purple'))


c.executemany('''INSERT INTO children_items (name, amount, children_id) VALUES(?, ?, ?)''',
          [('LEGO', 20, 1),('GIFT', 50, 1),('Green car', 5, 1), ('Green Care Bare', 20, 2),('GIFT', 50, 2),('CANDY', 15, 2)])

c.executemany('''INSERT INTO donar_sponsor_children (donar_id, children_id) VALUES (?,?)''',
          [(1,1),(1,2),(1,3),(1,4),(1,5)])


conn.commit()
