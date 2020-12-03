import aiohttp
from aiogram import types
from aiotgbot import dp

from aiotgbot.modules.help import add_command_help


@dp.message_handler(regexp='(meme[s]?$)')
async def memes(message: types.Message):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
            'https://some-random-api.ml/meme'
        ) as resp:
            r = await resp.json()
            await message.reply_photo(r['image'], caption=r['caption'])



add_command_help(
    'memes', [
        ['meme | memes', '| random memes (some-random-api.ml)'],
    ]
)