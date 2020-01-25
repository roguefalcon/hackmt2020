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
c.execute('''CREATE TABLE IF NOT EXISTS favorite_color
             (name text, color text)''')

c.execute('''CREATE TABLE IF NOT EXISTS users
             (username text, password text)''')

# Let's load some data
c.execute('''INSERT INTO users VALUES (?, ?)''',
          ('asdf', bcrypt.hashpw(b'asdf', bcrypt.gensalt())))
conn.commit()