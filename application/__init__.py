import sqlite3 
from flask import g
from application import main

# Database Connection =========================================================
@main.app.before_request
def db_connect():

    try:
        # The SQL connection ==================================================
        g.conn = sqlite3.connect('sql.db', check_same_thread=False)
        # This tells SQLite that I want dictionaries
        # instead of tuples for fetch statements
        g.conn.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(g.c.description)])
        # SQL cursor
        g.c = g.conn.cursor()
    except RuntimeError:
        print("FATAL: No database connection established")
