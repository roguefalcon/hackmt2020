#!/usr/bin/python3

# Imported libraries
import sqlite3

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

# Print favorite_color ========================================================
print("==> Favorite Colors")
c.execute('''SELECT * FROM favorite_color''')
colors = c.fetchall()

for color in colors:
    print(color)

# Print users =================================================================
print("==> Users")
c.execute('''SELECT * FROM users''')
users = c.fetchall()

for user in users:
    print(user)