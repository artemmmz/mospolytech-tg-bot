from aiogram import Router
from aiogram.types import Message

from app.core.commands import all_commands
from app.filters.commands import Commands

router = Router()


@router.message(Commands.START)
async def command_start(message: Message):

    await message.answer(
        'Привет! Я - удобный бот, который будет тебе присылать расписание вечером со всей информацией'
    )


@router.message(Commands.HELP)
async def command_help(message: Message):
    commands_lines = []
    for command in all_commands:
        commands_lines.append(
            f'\t - **/{command.command}** - {command.description}'
        )
    commands_text = '\n'.join(commands_lines)

    await message.answer(
        f'**Команды:** \n\n'
        f'{commands_text}\n\n'
        'Пусть ваша жизнь станет организованнее! 🌟',
        parse_mode='Markdown',
    )
