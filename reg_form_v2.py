"""
    Обновите форму регистрации из hw5/reg_form.py таким образом, чтобы:
    1. Все данные пользователей сохранялись в файл users.txt в любом формате.
    2. В файл errors.txt записывать все ошибочные либо не валидные вводы.
        (не валидный номер телефона, email и т.д.)
"""
from pathlib import Path
ok_path = Path('files/users.txt').resolve()
error_path = Path('files/errors.txt').resolve()


def main():
    phone_result = phone()
    email_result = email()
    len_str = pswd()
    asterisks = len(len_str)
    pass_result = ''.ljust(asterisks, '*')
    write_ok(f'Пароль {pass_result} принят')
    write_ok('')
    write_ok(
        'Поздравляем с успешной регистрацией!\n'
        f'Ваш номер телефона: {phone_result}\n'
        f'Ваш email: {email_result}\n'
        f'Ваш пароль: {pass_result}\n'
        )


def phone():
    while True:
        phone_input = input('Введите номер телефона: ')
        digits = ''
        for char in phone_input:
            if char.isdigit():
                digits += char
        if len(digits) >= 9:
            phone_input = '380' + digits[-9:]
        else:
            write_error(f'{phone_input} - неверный формат номера!')
            continue
        write_ok(f'Телефон "{phone_input}" записан.')
        return phone_input


def email():
    mail_length = ampersand = 0
    mail_input = None
    while mail_length < 6 or ampersand != 1:
        mail_input = input('Введите электропочту: ')
        mail_length = len(mail_input)
        ampersand = mail_input.count('@')
        if mail_length < 6 or ampersand != 1:
            write_error(f'{mail_input} - неверный формат почты! Необходимо 6 символов и @')
    write_ok(f'Электропочта "{mail_input}" записана.')
    return mail_input


def pswd():
    p_length = p_space = p_upper = p_lower = p_digit = 0
    pswd_input = None
    while p_length < 8 or p_space != 0 or p_upper < 1 or p_lower < 1 or p_digit < 1:
        p_length = p_space = p_upper = p_lower = p_digit = 0
        pswd_input = input('Введите пароль: ')
        p_length = len(pswd_input)
        for i in pswd_input:
            if str.isdigit(i):
                p_digit += 1
            elif str.islower(i):
                p_lower += 1
            elif str.isupper(i):
                p_upper += 1
            elif str.isspace(i):
                p_space += 1
        if p_length < 8 or p_space != 0 or p_upper < 1 or p_lower < 1 or p_digit < 1:
            write_error(f'{pswd_input} - неверный формат пароля! Повторите ввод!')
    ok_pass = input('Подтвердите пароль: ')
    if ok_pass == pswd_input:
        return pswd_input
    else:
        write_error('Пароли не совпадают! Повторите ввод!')
        return pswd()


def write_ok(ok):
    with open(ok_path, 'a') as f:
        print(ok)
        print(ok, file=f)
        f.close()


def write_error(error):
    with open(error_path, 'a') as f:
        print(error)
        print(error, file=f)
        f.close()


if __name__ == '__main__':
    main()