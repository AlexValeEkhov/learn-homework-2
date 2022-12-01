"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
list = [    {'name': 'Маша', 'age': 25, 'job': 'официантка'}, 
            {'name': 'Петя', 'age': 10, 'job': 'школьник'}, 
            {'name': 'Светлана', 'age': 48, 'job': 'главный бухгалтер'},
            {'name': 'Саша', 'age': 40, 'job': 'безработный'}
]

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('list.csv', 'w', encoding='utf-8') as file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(file, fields, delimiter=';')
        writer.writeheader()
        for person in list:
            writer.writerow(person)


if __name__ == "__main__":
    main()
