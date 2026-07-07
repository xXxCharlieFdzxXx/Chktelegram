import sqlite3
from datetime import datetime

conn = sqlite3.connect('syndicate.db', check_same_thread=False)
c = conn.cursor()

# Crear tablas
c.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    country TEXT DEFAULT 'MX',
    language TEXT DEFAULT 'es',
    active_key TEXT,
    plan_expires TEXT,
    max_mass INT DEFAULT 500
)''')

c.execute('''CREATE TABLE IF NOT EXISTS keys (
    key TEXT PRIMARY KEY,
    user_id INTEGER,
    days INT,
    expires_at TEXT,
    is_active BOOLEAN DEFAULT 1
)''')

c.execute('''CREATE TABLE IF NOT EXISTS lives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    card TEXT,
    gate TEXT,
    date TEXT
)''')

conn.commit()

def init_db():
    print("✅ Base de datos SQLite inicializada correctamente.")

def get_user(user_id: int):
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    return c.fetchone()

def save_live(user_id: int, card: str, gate: str = "Stripe"):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO lives (user_id, card, gate, date) VALUES (?, ?, ?, ?)",
              (user_id, card, gate, date))
    conn.commit()

init_db()    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount_xrp REAL,
    method TEXT,
    status TEXT,
    tx_id TEXT,
    date TEXT
)''')

c.execute('''CREATE TABLE IF NOT EXISTS user_proxies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    proxy TEXT,
    type TEXT,  -- http, socks4, socks5, residential
    is_valid BOOLEAN DEFAULT 0
)''')

c.execute('''CREATE TABLE IF NOT EXISTS residential_proxies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    proxy TEXT UNIQUE,
    validated_at TEXT,
    submitted_by INTEGER
)''')

conn.commit()

def get_user(user_id: int):
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    return c.fetchone()

def save_live(user_id: int, card: str, gate: str = "Stripe"):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO lives (user_id, card, gate, date) VALUES (?, ?, ?, ?)",
              (user_id, card, gate, date))
    conn.commit()

# Más funciones después...
print("✅ Base de datos SQLite inicializada correctamente.")
