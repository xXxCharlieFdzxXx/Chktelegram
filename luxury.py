import re
from datetime import datetime

def clean_cards(text: str):
    # Tu lógica del Luxury.py
    tarjetas = []
    patron = r'(\d{13,19})[^\d]*?(\d{2})[^\d]*?(\d{2,4})[^\d]*?(\d{3,4})'
    for m in re.finditer(patron, text):
        numero = re.sub(r'\D', '', m.group(1))
        mes = m.group(2)
        ano = m.group(3)
        cvv = m.group(4)
        if 13 <= len(numero) <= 19:
            tarjetas.append(f"{numero}|{mes}|{ano}|{cvv}")
    return tarjetas

async def luxury_handler(message):
    if message.document:
        file = await message.bot.get_file(message.document.file_id)
        content = await message.bot.download_file(file.file_path)
        text = content.read().decode()
        cleaned = clean_cards(text)
        await message.answer(f"✅ Limpiadas {len(cleaned)} tarjetas")
        # Guardar y enviar archivo
    else:
        await message.answer("Envía un archivo .txt")