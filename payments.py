from datetime import datetime, timedelta
from config import PLANS

async def generate_key(plan_type: str, user_id: int):
    plan = PLANS.get(plan_type)
    if not plan:
        return None
    expires = datetime.now() + timedelta(days=plan["days"])
    return f"KEY-{user_id}-{plan_type}-{int(datetime.now().timestamp())}", expires.strftime("%Y-%m-%d %H:%M")

# Más funciones de pago irán aquí después