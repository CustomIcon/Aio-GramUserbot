import asyncio
from aiogram.bot.api import TelegramAPIServer
import logging
from gpytranslate import Translator
from configparser import ConfigParser

from aiogram import Bot, Dispatcher

config = ConfigParser()
config.read('config.ini')


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(
        token=config.get('aiogram', 'usertoken'),
        server=TelegramAPIServer.from_base('https://bot.mannu.me')
    )
dp = Dispatcher(bot)

CMD_HELP = {}