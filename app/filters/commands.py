from aiogram.filters import CommandStart, Command

from app.utils.commands import BotCommands


class Commands:
    START: Command = CommandStart()
    HELP: Command = Command(
        BotCommands.HELP,
        ignore_case=True
    )
    SCHEDULE: Command = Command(
        BotCommands.SCHEDULE,
        ignore_case=True
    )
    SUBSCRIBE: Command = Command(
        BotCommands.SUBSCRIBE,
        ignore_case=True
    )
    UNSUBSCRIBE: Command = Command(
        BotCommands.UNSUBSCRIBE,
        ignore_case=True
    )
