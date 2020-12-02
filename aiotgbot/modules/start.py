from aiogram import types
from aiotgbot import dp

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply(
        "Hi!\nI'm AioTgBot!\nPowered by [aiogram](https://github.com/aiogram/aiogram).\n"
        "[Source](https://github.com/pokurt/Aio-GramUserbot)",
        parse_mode='Markdown',
        disable_web_page_preview=True
    )