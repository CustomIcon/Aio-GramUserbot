from aiogram import types
from aiotgbot import dp, CMD_HELP
from prettytable import PrettyTable
import asyncio


heading = "──「 **{0}** 」──\n"

def split_list(input_list, n):
    """
    Takes a list and splits it into smaller lists of n elements each.
    :param input_list:
    :param n:
    :return:
    """
    n = max(1, n)
    return [input_list[i:i + n] for i in range(0, len(input_list), n)]


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    cmd = message.text.split()
    help_arg = ""
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        help_arg = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        all_commands = ""
        all_commands += "Please specify which module you want help for!! \nUsage: `/help [module_name]`\n\n"

        ac = PrettyTable()
        ac.header = False
        ac.title = "AioTgBot Modules"
        ac.align = 'l'

        for x in split_list(sorted(CMD_HELP.keys()), 2):
            ac.add_row([x[0], x[1] if len(x) >= 2 else None])

        await message.reply(f"```{str(ac)}```",parse_mode='markdown')

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = "**Help for**\n"
            this_command += heading.format(str(help_arg)).upper()

            for x in commands:
                this_command += f"-> `{str(x)}`\n```{str(commands[x])}```\n"

            await message.reply(this_command, parse_mode='markdown')
        else:
            await message.reply('`Please specify a valid module name.`', parse_mode='markdown')


def add_command_help(module_name, commands):
    """
    Adds a modules help information.
    :param module_name: name of the module
    :param commands: list of lists, with command and description each.
    """

    command_dict = CMD_HELP[module_name] if module_name in CMD_HELP.keys() else {}
    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    CMD_HELP[module_name] = command_dict