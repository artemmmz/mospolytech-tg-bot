import datetime

from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.core.states import ScheduleState
from app.exceptions.invallid_argument import InvalidArgumentError
from app.exceptions.too_many_arguments import TooManyArgumentsError
from app.filters.callback_datas import ScheduleDate, ScheduleWeekday, Schedule
from app.filters.commands import Commands
from app.handlers.utils import answer_edit_message
from app.keyboards.inline.schedule import (get_schedule_date_keyboard,
                                           get_schedule_weekday_keyboard)
from app.services.schedule import ScheduleService
from app.utils.date import get_weekday
from app.utils.dicts import WEEKDAYS_PLURALS
from app.utils.enums import Weekday
from app.utils.texts import get_schedule_text
from app.utils.utils import get_weekday_by_word

router = Router()


async def __schedule(message: Message, state: FSMContext) -> None:
    await state.set_state(ScheduleState.GROUP)

    await message.answer('Введите группу')


async def __schedule_weekday(
    message: Message,
    group: str,
    weekday: Weekday,
    schedule_service: ScheduleService,
    is_edit: bool = False,
) -> None:
    all_schedule = await schedule_service.get_schedule(group)
    weekday_schedule = all_schedule.lessons[weekday.value]

    schedule_text = get_schedule_text(weekday_schedule)
    weekday_plural = WEEKDAYS_PLURALS[weekday][3]

    answer_text = (
        f'🎓 Расписание для группы {group} на '
        f'{weekday_plural} 🎓\n\n'
        f'{schedule_text}\n'
        f'✨ Желаем успешного и продуктивного дня! 📚🌟'
    )
    reply_markup = get_schedule_weekday_keyboard(group, weekday)
    await answer_edit_message(
        message,
        answer_text,
        is_edit,
        parse_mode=ParseMode.HTML,
        reply_markup=reply_markup,
    )


async def __schedule_month(
    message: Message,
    group: str,
    date: str,
    schedule_service: ScheduleService,
    is_edit: bool = False,
) -> None:
    all_schedule = await schedule_service.get_schedule(group)
    formatted_date = datetime.date.fromisoformat(date)

    date_weekday = get_weekday(formatted_date)
    date_schedule = all_schedule.lessons[date_weekday]

    schedule_text = get_schedule_text(date_schedule, formatted_date)
    answer_text = (
        f'🎓 Расписание для группы {group} на '
        f'{formatted_date.strftime("%d %b (%A)")} 🎓\n\n'
        f'{schedule_text}\n'
        f'✨ Желаем успешного и продуктивного дня! 📚🌟'
    )
    await answer_edit_message(
        message,
        answer_text,
        is_edit,
        parse_mode=ParseMode.HTML,
        reply_markup=get_schedule_date_keyboard(group, formatted_date),
    )


@router.message(Commands.SCHEDULE)
async def command_schedule(
    message: Message,
    command: CommandObject,
    schedule_service: ScheduleService,
    state: FSMContext,
) -> None:
    if command.args is None:
        return await __schedule(message, state)
    arguments = command.args.strip().split(' ')
    group = arguments[0]
    if len(arguments) == 1:
        weekday = get_weekday()
    elif len(arguments) == 2:
        weekday = get_weekday_by_word(arguments[1])
    else:
        raise TooManyArgumentsError(2, len(arguments))

    if weekday is None:
        raise InvalidArgumentError('день недели')

    return await __schedule_weekday(message, group, weekday, schedule_service)


@router.message(ScheduleState.GROUP)
async def schedule_group(
    message: Message, schedule_service: ScheduleService, state: FSMContext
) -> None:
    await state.set_state(None)

    group = message.text.strip()
    weekday = get_weekday()
    return await __schedule_weekday(message, group, weekday, schedule_service)


@router.callback_query(Schedule.filter())
async def callback_schedule(
        callback_query: CallbackQuery, state: FSMContext
) -> None:
    await callback_query.message.edit_reply_markup()
    await __schedule(callback_query.message, state)


@router.callback_query(ScheduleWeekday.filter())
async def callback_schedule_weekday(
    callback_query: CallbackQuery,
    callback_data: ScheduleWeekday,
    schedule_service: ScheduleService,
) -> None:
    group = callback_data.group
    weekday = callback_data.weekday

    await __schedule_weekday(
        callback_query.message, group, weekday, schedule_service, is_edit=True
    )


@router.callback_query(ScheduleDate.filter())
async def callback_schedule_date(
    callback_query: CallbackQuery,
    callback_data: ScheduleDate,
    schedule_service: ScheduleService,
) -> None:
    group = callback_data.group
    date = callback_data.date

    await __schedule_month(
        callback_query.message, group, date, schedule_service, is_edit=True
    )
