from gpytranslate import Translator
from aiogram import types
from aiotgbot import dp

from aiotgbot.modules.help import add_command_help


@dp.message_handler(commands=['tr'])
async def do_translate(message: types.Message):
    trl = Translator()
    if message.reply_to_message and (message.reply_to_message.text or message.reply_to_message.caption):
        if len(message.text.split()) == 1:
            await message.delete()
            return
        target = message.text.split()[1]
        if message.reply_to_message.text:
            text = message.reply_to_message.text
        else:
            text = message.reply_to_message.caption
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await message.reply(f"Error: `{str(err)}`", parse_mode='Markdown')
            return
    else:
        if len(message.text.split()) <= 2:
            await message.delete()
            return
        target = message.text.split(None, 2)[1]
        text = message.text.split(None, 2)[2]
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await message.reply("Error: `{}`".format(str(err)), parse_mode='Markdown')
            return

    await message.reply(f"*Translated:*\n```{tekstr.text}```\n\n*Detected Language:* `{(await trl.detect(text))}`", parse_mode='Markdown')


add_command_help(
    'Translate', [
        ['/tr', 'Google Translate (@DavideGalilei)'],
    ]
)