import asyncio
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import save_live
# from proxypool import proxy_pool  # Integra tu pool aquí

router = Router()

async def check_card(card: str) -> dict:
    await asyncio.sleep(1)  # Simula tiempo real
    return {"status": "LIVE", "type": "Visa", "level": "Classic", "country": "MX"}

class CheckStates(StatesGroup):
    mass_check = State()

@router.message(CheckStates.mass_check)
async def process_mass_check(message: Message, state: FSMContext):
    await message.answer("📊 Iniciando Mass Check...")
    # Lógica de procesamiento en batch con progreso aquí
    await state.clear()

@router.callback_query(F.data == "cancel_check")
async def cancel_process(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("⛔ Proceso cancelado.")
    await state.clear()
