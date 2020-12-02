import importlib
from aiotgbot.modules import ALL_MODULES
from aiotgbot import dp
from aiogram import executor


for module in ALL_MODULES:
    imported_module = importlib.import_module("aiotgbot.modules." + module)
    importlib.reload(imported_module)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)