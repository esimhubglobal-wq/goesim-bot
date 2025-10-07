import os
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
SIMO_URL = os.getenv("SIMO_URL", "")

if not BOT_TOKEN:
    raise RuntimeError("Environment variable BOT_TOKEN is not set")

bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(m: types.Message):
    text = (
        "Привет! Я Go_ESIM бот.\n"
        "Хочешь быстрый eSIM для путешествий? 👉 <a href='{0}'>Оформить</a>\n"
        "Напиши мне страну или город — подскажу, как выгоднее подключиться."
    ).format(SIMO_URL or "https://t.me/Go_ESIM")
    await m.answer(text, disable_web_page_preview=True)

    if ADMIN_ID and m.from_user.id != ADMIN_ID:
        u = m.from_user
        uname = f'@{u.username}' if u.username else "(без username)"
        await bot.send_message(ADMIN_ID, f"Новый пользователь: {u.id} {uname}")

@dp.message_handler()
async def fallback(m: types.Message):
    await m.answer("Напиши /start, чтобы начать 🙂")

if __name__ == "__main__":
    logging.info("Bot starting…")
    executor.start_polling(dp, skip_updates=True)
