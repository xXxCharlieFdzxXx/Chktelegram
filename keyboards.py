from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔍 Single Check", callback_data="single")],
        [InlineKeyboardButton(text="📁 Mass Check", callback_data="mass")],
        [InlineKeyboardButton(text="🔑 Redeem Key", callback_data="redeem")],
        [InlineKeyboardButton(text="⚙️ Proxies", callback_data="proxies")],
        [InlineKeyboardButton(text="✨ Luxury", callback_data="luxury")],
        [InlineKeyboardButton(text="👑 Admin Panel", callback_data="admin_panel")],  # Solo visible para admin
    ])

def admin_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📊 Estadísticas", callback_data="stats")],
        [InlineKeyboardButton(text="🔑 Generar Keys", callback_data="generate_key")],
        [InlineKeyboardButton(text="💰 Ajustar Precios", callback_data="adjust_prices")],
        [InlineKeyboardButton(text="🔄 Recargar Proxies Global", callback_data="reload_proxies")],
        [InlineKeyboardButton(text="👥 Usuarios Activos", callback_data="active_users")],
        [InlineKeyboardButton(text="📋 Ver Todas Lives", callback_data="all_lives")],
        [InlineKeyboardButton(text="🏠 Volver al Menú", callback_data="back_to_main")]
    ])

def proxies_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌐 HTTP Proxies", callback_data="proxies_http")],
        [InlineKeyboardButton(text="🔄 SOCKS4", callback_data="proxies_socks4")],
        [InlineKeyboardButton(text="🔄 SOCKS5", callback_data="proxies_socks5")],
        [InlineKeyboardButton(text="🏠 Residential", callback_data="proxies_residential")],
        [InlineKeyboardButton(text="➕ Agregar Mis Proxies", callback_data="add_proxies")],
        [InlineKeyboardButton(text="🗑️ Delete All Proxies", callback_data="delete_proxies")],
        [InlineKeyboardButton(text="🏠 Volver", callback_data="back_to_main")]
    ])

def cancel_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⛔ Cancelar Proceso", callback_data="cancel_check")]
    ])
