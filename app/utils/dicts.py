"""Module with all dictionaries."""

from app.utils.enums import Weekday

WEEKDAYS = {
    Weekday.MONDAY: 'понедельник',
    Weekday.TUESDAY: 'вторник',
    Weekday.WEDNESDAY: 'среда',
    Weekday.THURSDAY: 'четверг',
    Weekday.FRIDAY: 'пятница',
    Weekday.SATURDAY: 'суббота',
}

WEEKDAYS_VARIABLES = {
    Weekday.MONDAY: ['пн', 'mon', 'понедельник', 'monday'],
    Weekday.TUESDAY: ['вт', 'tue', 'вторник', 'tuesday'],
    Weekday.WEDNESDAY: ['ср', 'wed', 'среда', 'wednesday'],
    Weekday.THURSDAY: ['чт', 'thu', 'четверг', 'thursday'],
    Weekday.FRIDAY: ['пт', 'fr', 'пятница', 'friday'],
    Weekday.SATURDAY: ['сб', 'sat', 'суббота', 'saturday'],
}

WEEKDAYS_PLURALS = {
    Weekday.MONDAY: [
        'понедельник',
        'понедельника',
        'понедельнику',
        'понедельник',
        'понедельником',
        'понедельнике',
    ],
    Weekday.TUESDAY: [
        'вторник',
        'вторника',
        'вторнику',
        'вторник',
        'вторником',
        'вторнике',
    ],
    Weekday.WEDNESDAY: ['среда', 'среды', 'среде', 'среду', 'средой', 'среде'],
    Weekday.THURSDAY: [
        'четверг',
        'четверга',
        'четвергу',
        'четверг',
        'четвергом',
        'четверге',
    ],
    Weekday.FRIDAY: [
        'пятница',
        'пятницы',
        'пятнице',
        'пятницу',
        'пятницей',
        'пятнице',
    ],
    Weekday.SATURDAY: [
        'суббота',
        'субботы',
        'субботе',
        'субботу',
        'субботой',
        'субботе',
    ],
}

SCHEDULE_TIMES = [
    "9:00-10:30",
    "10:40-12:10",
    "12:20-13:50",
    "14:30-16:00",
    "16:10-17:40",
    "17:50-19:20",
    "19:30-21:00",
]
