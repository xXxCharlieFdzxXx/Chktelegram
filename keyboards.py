from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔍 Single Check", callback_data="single")],
        [InlineKeyboardButton(text="📁 Mass Check", callback_data="mass")],
        [InlineKeyboardButton(text="🔑 Redeem Key", callback_data="redeem")],
        [InlineKeyboardButton(text="⚙️ Ajustes", callback_data="settings")],
        [InlineKeyboardButton(text="🎁 Free", callback_data="free")],
        [InlineKeyboardButton(text="✨ Luxury", callback_data="luxury")]
    ])

def admin_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📊 Estadísticas", callback_data="stats")],
        [InlineKeyboardButton(text="🔑 Generar Key", callback_data="generate_key")],
        [InlineKeyboardButton(text="💰 Ajustar Precios", callback_data="adjust_prices")],
        [InlineKeyboardButton(text="🔄 Recargar Proxies", callback_data="reload_proxies")]
    ])