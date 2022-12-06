"""Минимум 8 символов, хотя бы 1а большая буква, хотя бы 3 цифры"""


def new_input():
    new_password = input('Придумайте пароль: ')
    return new_password


def ver_of_high_symb(symb_password: str):
    if list(filter(str.isupper, symb_password)):
        return True


def ver_of_digits(digit_password: str):
    if len(list(filter(str.isdigit, digit_password))) >= 3:
        return True


def verification(password: str):
    if len(password) > 8 and ver_of_high_symb(password) and ver_of_digits(password):
        print('Это надёжный пароль!')
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        verification(new_input())
    pass


if __name__ == '__main__':
    verification(new_input())
