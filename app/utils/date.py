"""Module with functions for working with dates and times."""

import datetime

from dateutil.relativedelta import relativedelta
from dateutil.tz import tz

from app.utils.enums import Weekday


def get_now() -> datetime.datetime:
    """
    Get current date and time.

    :return: Current date and time.
    """
    return datetime.datetime.now(tz=tz.tzoffset("Europe/Moscow", 3))


def get_week_now() -> int:
    """
    Get current week number.

    :return: Current week.
    """
    week = get_now().isocalendar()[1]
    return week


def get_year_now() -> int:
    """
    Get current year.

    :return: Current year.
    """
    year = get_now().year
    return year


def get_weekday(date: datetime.date = None) -> Weekday:
    """
    Get Weekday instance from date.

    :param date: Date, just date.
    :return: Weekday instance.
    """
    if date is None:
        date = get_now()

    index = date.weekday()
    if index == 6:
        index = 0
    return list(Weekday)[index]


def get_next_month(date: datetime.date) -> datetime.date:
    """
    Get instance of date with next month.

    :param date: Date, just, date.
    :return: New instance of date.
    """
    new_date = date + relativedelta(months=1)
    if new_date.weekday() == 6:
        new_date += relativedelta(days=1)
    return new_date


def get_previous_month(date: datetime.date) -> datetime.date:
    """
    Get new instance of date with previous month.

    :param date: Date, just date.
    :return: New instance of date.
    """
    new_date = date - relativedelta(months=1)
    if new_date.weekday() == 6:
        new_date += relativedelta(days=1)
    return new_date


def get_next_day(date: datetime.date) -> datetime.date:
    """
    Get new instance of date with next day.

    :param date: Date, just date
    :return: New instance of date.
    """
    next_day = 1
    if date.weekday() == 5:
        next_day = 2
    return date + datetime.timedelta(days=next_day)


def get_previous_day(date: datetime.date) -> datetime.date:
    """
    Get new instance of date with previous day.

    :param date: Date, just date, random date.
    :return: New instance of date.
    """
    previous_day = 1
    if date.weekday() == 0:
        previous_day = 2
    return date - datetime.timedelta(days=previous_day)
