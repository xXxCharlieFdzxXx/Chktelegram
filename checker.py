import asyncio
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from database import save_live
from proxypool import proxy_pool  # Tu pool original

router = Router()

async def check_card(card: str) -> dict:
    """Tu lógica real de checker aquí"""
    # Ejemplo simulado
    await asyncio.sleep(1.5)
    return {
        "status": "LIVE",
        "type": "Visa",
        "level": "Classic",
        "country": "MX",
        "gate": "Stripe Auth"
    }

@router.message()
async def process_check(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if not current_state:
        return

    card = message.text.strip()
    result = await check_card(card)

    if result["status"] == "LIVE":
        save_live(message.from_user.id, card, result["gate"])
        await message.answer(f"✅ **LIVE**\n{card}\n{result['type']} {result['level']} {result['country']}")
    else:
        await message.answer("❌ Declined")

    await state.clear()
