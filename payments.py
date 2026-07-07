import asyncio
from datetime import datetime, timedelta
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import PLANS, ADMIN_ID

router = Router()

async def get_crypto_price(symbol: str) -> float:
    # Simulado - reemplaza con API real (CoinGecko)
    prices = {"XRP": 0.55, "BTC": 62000, "ETH": 2550}
    return prices.get(symbol, 0.55)

@router.callback_query(F.data.startswith("pay_"))
async def handle_payment(call: CallbackQuery, state: FSMContext):
    plan_key = call.data.split("_")[1]
    plan = PLANS.get(plan_key, PLANS["1m"])
    await call.message.edit_text(f"💰 Plan {plan_key} - ${plan['price_xrp']} XRP\nElige método:", 
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="XRP (Descuento)", callback_data=f"crypto_xrp_{plan_key}")],
            [InlineKeyboardButton(text="BTC", callback_data=f"crypto_btc_{plan_key}")],
            [InlineKeyboardButton(text="ETH", callback_data=f"crypto_eth_{plan_key}")],
        ]))

# Más lógica de QR y timer de 120 segundos aquí (te la mando en el siguiente bloque si quieres)
