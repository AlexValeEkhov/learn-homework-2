"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import *

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date = datetime.now()
    delta_yes = timedelta(days=-1)
    delta_month_ahead = timedelta(days=30)
    print(date)
    print(date + delta_yes)
    print(date + delta_month_ahead)


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
