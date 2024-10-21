from aiogram.types import BotCommand


class BotCommands:
    HELP = BotCommand(
        command='help',
        description='Показать меню со всеми доступными командами. '
        'Используй, чтобы быстро узнать, какие функции '
        'доступны и как ими пользоваться.',
    )
    SCHEDULE = BotCommand(
        command='schedule',
        description='Узнать расписание занятий. '
        'Позволяет получить информацию о '
        'расписании для определённой группы '
        'на указанный день. Примеры использования:\n'
        '\t\t`/schedule 241-331 понедельник` - '
        'Показывает расписание семестра для '
        'группы 241-331 на понедельник.\n'
        # '\t\t`/schedule 241-331 24 октября` - '
        # 'Даёт расписание на конкретный день.\n'
        '\t\t`/schedule 241-331` - '
        'Показывает расписание на текущий день недели.',
    )
    SUBSCRIBE = BotCommand(
        command='subscribe',
        description='Подписаться на ежедневное получение расписания. '
        'Ты можешь настроить время, в которое бот будет '
        'присылать расписание, чтобы не пропустить занятия.'
        '(Команда ещё не готова)',
    )
    UNSUBSCRIBE = BotCommand(
        command='unsubscribe',
        description='Отписаться от рассылки расписания. '
        'Используй эту команду, если больше не '
        'хочешь получать расписание автоматически.'
        '(Команда ещё не готова)',
    )


all_commands = [
    BotCommands.HELP,
    BotCommands.SCHEDULE,
    BotCommands.SUBSCRIBE,
    BotCommands.UNSUBSCRIBE,
]
