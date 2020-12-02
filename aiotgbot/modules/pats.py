from aiogram import types
from aiotgbot import dp
import aiohttp

from aiotgbot.modules.help import add_command_help


@dp.message_handler(regexp='(^pat[s]?$|pat)')
async def pats(message: types.Message):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
            'https://some-random-api.ml/animu/pat'
        ) as resp:
            r = await resp.json()
            await message.reply_animation(r['link'], caption='*Pats* goodboi >~<')



add_command_help(
    'pat', [
        ['pat | pats', '| pat gifs (some-random-api.ml)'],
    ]
)