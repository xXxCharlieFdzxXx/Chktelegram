import sqlite3
from datetime import datetime

conn = sqlite3.connect('syndicate.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users 
             (user_id INTEGER PRIMARY KEY, username TEXT, country TEXT, plan_expires TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS lives 
             (id INTEGER PRIMARY KEY, user_id INTEGER, card TEXT, gate TEXT, date TEXT)''')

conn.commit()

def save_live(user_id, card, gate="Stripe"):
    c.execute("INSERT INTO lives (user_id, card, gate, date) VALUES (?, ?, ?, ?)",
              (user_id, card, gate, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()