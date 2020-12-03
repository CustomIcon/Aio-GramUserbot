import aiohttp
from aiogram import types
from aiotgbot import dp

from aiotgbot.modules.help import add_command_help


@dp.message_handler(commands=['mc'])
async def memes(message: types.Message):
    try:
        mc_username = message.text.split()[1]
    except IndexError:
        await message.reply('try `/mc` `your_minecraft_username`', parse_mode='markdown')
        return
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
            'https://some-random-api.ml/mc?username=' + mc_username
        ) as resp:
            r = await resp.json()
    try:
        text = f'*Username:* `{r["username"]}`\n'
        text += f'*UUID:* `{r["uuid"]}`\n'
        text += f'\n*Username History:*\n'
        for u in r["name_history"]:
            text += f'`{u["name"]}`\n'
    except KeyError:
        text = 'Minecraft Username Invalid!'
    await message.reply(text, parse_mode='markdown')



add_command_help(
    'minecraft', [
        ['/mc', '| get minecraft account details (some-random-api.ml)'],
    ]
)