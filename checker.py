import asyncio
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from database import save_live
# from proxypool import proxy_pool  # Descomenta cuando lo integres

router = Router()

async def check_card(card: str):
    await asyncio.sleep(1.5)  # Simula chequeo
    return {"status": "LIVE", "details": "Visa Classic MX"}

@router.message()
async def process_card(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if not current_state:
        return
    result = await check_card(message.text)
    if result["status"] == "LIVE":
        save_live(message.from_user.id, message.text)
        await message.answer(f"✅ **LIVE** {message.text}")
    else:
        await message.answer("❌ Declined")
    await state.clear()
