from aiogram import Router
from aiogram.types import Message, CallbackQuery

from app.core.commands import all_commands
from app.filters.commands import Commands
from app.keyboards.inline.basic_inline import HELP_KEYBOARD

router = Router()


@router.message(Commands.START)
async def command_start(message: Message):
    await message.answer(
        'Привет! Я - удобный бот, который будет тебе присылать расписание вечером со всей информацией'
    )
    await command_help(message)


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
        reply_markup=HELP_KEYBOARD
    )


@router.callback_query()
async def callback_help(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup()

    await command_help(callback_query.message)
