from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from config import ADMIN_ID
from keyboards import main_menu, admin_menu

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("👑 Bienvenido Admin", reply_markup=admin_menu())
    else:
        await message.answer("🌍 Bienvenido a THE SYNDICATE CHECEKR\nSelecciona una opción:", reply_markup=main_menu())

@router.callback_query()
async def callbacks(call: CallbackQuery):
    if call.data == "single":
        await call.message.edit_text("Envía la tarjeta en formato: `cc|mm|yy|cvv`")
    elif call.data == "mass":
        await call.message.edit_text("Envía el archivo .txt con las tarjetas")
    elif call.data == "admin" and call.from_user.id == ADMIN_ID:
        await call.message.edit_text("Panel Admin", reply_markup=admin_menu())
    await call.answer()