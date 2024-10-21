from enum import Enum

from aiogram.types import BotCommand


class BotCommands:
    HELP = BotCommand(command='help', description='Help command')
    SCHEDULE = BotCommand(command='schedule', description='Schedule command')
    SUBSCRIBE = BotCommand(command='subscribe', description='Subscribe command')
    UNSUBSCRIBE = BotCommand(command='unsubscribe', description='Unsubscribe command')

all_commands = [
    BotCommands.HELP,
    BotCommands.SCHEDULE,
    BotCommands.SUBSCRIBE,
    BotCommands.UNSUBSCRIBE
]
