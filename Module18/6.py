"""Получить из строки aaAAbbсaaaA  = a2A2b2с1a3A1 """
import re


def new_input():
    # new_word = input('Введите строку: ')
    return 'aaAAbbсaaaA'


def cash_string(new_string: str):
    result = re.findall(r'(([\w+])\2)', new_string)
    if result:
        print(result)
    pass


cash_string('aaAAbbсaaaA')
