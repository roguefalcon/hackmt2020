#!/usr/bin/python3

# Imported libraries
import sqlite3

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

# Print favorite_color ========================================================
print("==> children")
c.execute('''SELECT * FROM children''')
children = c.fetchall()

for child in children:
    print(child)

# Print children_items =======================================================
print("==> children_items")
c.execute('''SELECT * FROM children_items''')
children_items = c.fetchall()

for item in children_items:
    print(item)

c.execute('''SELECT * FROM children LEFT JOIN  children_items ON children_items.children_id = children.id where children.id = 1''')

children_array = c.fetchall()

for children in children_array:
    print(children)

#print donors:
print("==> donors")
c.execute('''SELECT * FROM donor''')
donor = c.fetchall()

for item  in donor:
    print(item)

#Print Donar_sponsor_children
print("==> donar_sponsor_children")
c.execute('''SELECT * FROM donar_sponsor_children''')
donar_sponsor_children = c.fetchall()

for associations in donar_sponsor_children:
    print(associations)
# Print users =================================================================
#print("==> Users")
#c.execute('''SELECT * FROM users''')
#users = c.fetchall()

#for user in users:
#    print(user)
