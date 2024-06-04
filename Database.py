import os
import sqlite3

def create_connection():
    conn = sqlite3.connect('CustomerDatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                      id INTEGER PRIMARY KEY,
                      name TEXT,
                      contact TEXT,
                      address TEXT,
                      left_eye_degree REAL,
                      right_eye_degree REAL)''')
    conn.commit()
    cursor.close()
    return conn

def insert_customer(name, contact, address, left_eye_degree, right_eye_degree):
    conn = create_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO customers (name, contact, address, left_eye_degree, right_eye_degree)
    VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(query, (name, contact, address, left_eye_degree, right_eye_degree))
    conn.commit()
    cursor.close()
    conn.close()

def fetch_customers():
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM customers"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

insert_customer('Satoshi Nakamoto', 'nakamoto@proton.com', '1-7-1 Konan, Minato-ku, Tokyo 108-0075, Japan', -1.25, -0.75)
insert_customer('Guido van Rossum', 'rossum@gmail.com', '1600 Amphitheatre Parkway, Mountain View, CA 94043, USA', +2.25, +1.75)
insert_customer('Markus Alexej Persson', 'notch@hotmail.com', 'Maria Skolgata 83, 118 53 Stockholm, Sweden', +0.25, -0.50)
insert_customer('Hidetaka Miyazaki', 'miyazaki@icloud.com', '1000 Flower Street, Glendale, CA 91201, USA', -3.25, -2.05)
customers = fetch_customers()
for customer in customers:
    print(customer)
