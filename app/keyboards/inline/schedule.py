import datetime

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.filters.callback_datas import ScheduleDate, ScheduleWeekday
from app.utils.date import (get_next_day, get_next_month, get_now,
                            get_previous_day, get_previous_month, get_weekday)
from app.utils.dicts import WEEKDAYS
from app.utils.enums import Weekday


def get_schedule_weekday_keyboard(
    group: str, weekday: Weekday
) -> InlineKeyboardMarkup:
    date_now = get_now().date()
    weekday_now = get_weekday()

    builder = InlineKeyboardBuilder()

    builder.button(
        text='<-',
        callback_data=(
            ScheduleWeekday(group=group, weekday=weekday.previous)
            if weekday != Weekday.MONDAY
            else 'nothing'
        ),
    )
    builder.button(
        text=WEEKDAYS[weekday].title(),
        callback_data=(
            ScheduleWeekday(group=group, weekday=weekday_now)
            if weekday != weekday_now
            else 'nothing'
        ),
    )
    builder.button(
        text='->',
        callback_data=(
            ScheduleWeekday(group=group, weekday=weekday.next)
            if weekday != Weekday.SATURDAY
            else 'nothing'
        ),
    )

    builder.button(text='В меню', callback_data='nothing')
    builder.button(
        text='Дата',
        callback_data=ScheduleDate(group=group, date=date_now.isoformat()),
    )
    builder.adjust(3, 2)
    return builder.as_markup()


def get_schedule_date_keyboard(
    group: str, date: datetime.date
) -> InlineKeyboardMarkup:
    date_now = get_now().date()
    weekday_now = get_weekday(date)

    builder = InlineKeyboardBuilder()

    builder.button(
        text='<-',
        callback_data=ScheduleDate(
            group=group, date=get_previous_day(date).isoformat()
        ),
    )
    builder.button(
        text=f'{date.day} день',
        callback_data=(
            ScheduleDate(group=group, date=date_now.isoformat())
            if date != date_now
            else 'nothing'
        ),
    )
    builder.button(
        text='->',
        callback_data=ScheduleDate(
            group=group, date=get_next_day(date).isoformat()
        ),
    )

    builder.button(
        text='<-',
        callback_data=ScheduleDate(
            group=group, date=get_previous_month(date).isoformat()
        ),
    )
    builder.button(
        text=f'{date.strftime("%B")}',
        callback_data=(
            ScheduleDate(
                group=group,
                date=(date.replace(month=date_now.month)).isoformat(),
            )
            if date.month != date_now.month
            else 'nothing'
        ),
    )
    builder.button(
        text='->',
        callback_data=ScheduleDate(
            group=group, date=get_next_month(date).isoformat()
        ),
    )

    builder.button(text='В меню', callback_data='nothing')
    builder.button(
        text='Семестр',
        callback_data=ScheduleWeekday(group=group, weekday=weekday_now),
    )

    builder.adjust(3, 3, 2)
    return builder.as_markup()
