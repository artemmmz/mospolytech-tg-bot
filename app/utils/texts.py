"""Texts variables and functions."""

import datetime
from typing import Dict

from app.core.schedule import Lesson
from app.utils.dicts import SCHEDULE_TIMES

EMPTY_SCHEDULE_TEXT = (
    'В этот день нет занятий. Используйте этот день для '
    'самоподготовки, отдыха или развития навыков.\n'
)


def get_schedule_text(
    schedule: Dict[str, list[Lesson]],
    date: datetime.date | str | None = None,
) -> str:
    """
    Get schedule text in a day.

    :param schedule: Schedule weekday.
    :param date: (optional) Date to get schedule text for.
    :return: Schedule text.
    """
    if isinstance(date, str):
        date = datetime.date.fromisoformat(date)

    schedule_lines = []
    for lesson_num, lessons in schedule.items():
        for lesson in lessons:
            if (
                date is not None
                and not lesson.date_from <= date <= lesson.date_to
            ):
                continue
            schedule_time = SCHEDULE_TIMES[int(lesson_num) - 1]
            schedule_lines.append(
                f'{lesson_num}. 🕒 {schedule_time}\n'
                f'\t{lesson.subject} 📚 ({lesson.type})\n'
                f'\t📅 {lesson.dates_str}\n'
                f'\t👩‍🏫 {lesson.teacher}\n'
                f'\t🏫 {lesson.auditories_text}\n'
            )
    if len(schedule_lines) == 0:
        return EMPTY_SCHEDULE_TEXT
    return '\n'.join(schedule_lines)
