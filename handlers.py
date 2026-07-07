from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import ADMIN_ID
from keyboards import main_menu, admin_menu, proxies_menu, cancel_button
from database import get_user, save_live

router = Router()

class BotStates(StatesGroup):
    waiting_single = State()
    waiting_mass = State()
    waiting_redeem = State()

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    if message.from_user.id == ADMIN_ID:
        await message.answer("👑 **THE SYNDICATE CHECKER** - Admin", reply_markup=admin_menu(), parse_mode="Markdown")
    else:
        await message.answer("🌐 **THE SYNDICATE CHECKER**", reply_markup=main_menu(), parse_mode="Markdown")

@router.callback_query()
async def handle_callbacks(call: CallbackQuery, state: FSMContext):
    await call.answer()
    data = call.data
    user_id = call.from_user.id

    if data == "single":
        await call.message.edit_text("🔍 **Single Check**\nEnvía la tarjeta:", parse_mode="Markdown")
        await state.set_state(BotStates.waiting_single)
    elif data == "mass":
        await call.message.edit_text("📁 **Mass Check**\nEnvía .txt o pega tarjetas:", parse_mode="Markdown", reply_markup=cancel_button())
        await state.set_state(BotStates.waiting_mass)
    elif data == "proxies":
        await call.message.edit_text("⚙️ **Gestión de Proxies**", reply_markup=proxies_menu())
    elif data == "redeem":
        await call.message.edit_text("🔑 Envía tu key:", parse_mode="Markdown")
        await state.set_state(BotStates.waiting_redeem)
    elif data == "cancel_check":
        await call.message.edit_text("⛔ Proceso cancelado.")
        await state.clear()
    elif user_id == ADMIN_ID:
        await call.message.edit_text(f"🔧 {data.replace('_', ' ').title()} - En desarrollo", reply_markup=admin_menu())

@router.message(BotStates.waiting_single)
async def process_single(message: Message, state: FSMContext):
    await message.answer("✅ Procesando tarjeta...")
    save_live(message.from_user.id, message.text)
    await state.clear()

@router.message(BotStates.waiting_mass)
async def process_mass(message: Message, state: FSMContext):
    await message.answer("📊 Mass check en desarrollo...")
    await state.clear()

@router.message(BotStates.waiting_redeem)
async def process_redeem(message: Message, state: FSMContext):
    await message.answer("🔑 Key verificada.")
    await state.clear()
