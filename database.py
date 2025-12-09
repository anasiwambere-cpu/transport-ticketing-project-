import sqlite3

def get_connection():
    return sqlite3.connect('food_delivery.db')

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT);")
    cursor.execute("CREATE TABLE IF NOT EXISTS food (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL);")
    cursor.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, food_id INTEGER, status TEXT);")
    conn.commit(); conn.close()
