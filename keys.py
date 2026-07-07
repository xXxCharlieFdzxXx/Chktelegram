import uuid
from datetime import datetime, timedelta
from database import conn, c

def generate_key(days: int) -> str:
    key = "SYND-" + str(uuid.uuid4())[:8].upper()
    c.execute("INSERT INTO keys (key, days, expires_at) VALUES (?, ?, ?)", 
              (key, days, (datetime.now() + timedelta(days=days)).isoformat()))
    conn.commit()
    return key

def redeem_key(user_id: int, key: str) -> bool:
    c.execute("SELECT * FROM keys WHERE key = ? AND is_active = 1", (key,))
    row = c.fetchone()
    if row:
        c.execute("UPDATE keys SET is_active = 0, user_id = ? WHERE key = ?", (user_id, key))
        conn.commit()
        return True
    return False
