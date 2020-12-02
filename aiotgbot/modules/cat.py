from aiogram import types
from aiotgbot import dp
import aiohttp

from aiotgbot.modules.help import add_command_help


@dp.message_handler(regexp='(^cat[s]?$|pussy)')
async def cats(message: types.Message):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
            'https://api.thecatapi.com/v1/images/search'
        ) as resp:
            r = await resp.json()
            await message.reply_photo(r[0]['url'], caption='Cats are here 😺')


add_command_help(
    'Cat', [
        ['cat | cats | pussy', 'neko pics (thecatapi.com)'],
    ]
)