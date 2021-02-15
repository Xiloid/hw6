"""
    Текстовый файл (phone_book.txt) содержит список из имен и номеров телефона.
    Переписать в файл (edited_phone_book.txt) данные владельцев,
    чьи имена начинаются на букву "m" либо заканчиваются на "а"
    (регистр не имеет значения).
    В файл записывать данные в таком формате:
    1. +380501234561 - Имя
    2. +380501234562 - Имя
    3. +380501234563 - Имя
    4. +380501234564 - Имя
"""
import re
import string
from pathlib import Path
in_path = Path('files/phone_book.txt').resolve()
out_path = Path('files/edited_phone_book.txt').resolve()


def main():
    name = phone = None
    with open(in_path, 'r') as f:
        f.seek(0)
        for line in f.readlines():
            f.seek(0)
            list_name = re.findall(r'[a-zA-Z]', line)
            list_phone = re.findall(r'\d', line)
            name = ''.join(list_name)
            phone = ''.join(list_phone)
            name = name.capitalize()
            if name.find('M') == 0 or name.rfind('a') == len(name) - 1:


'''
def do_name(name):
    with open(in_path, 'w') as f:
        pass


def jnjnj():
    with open(in_path, 'r') as f:
        f.seek(0)
        for line in f.readlines():
            pass



def phone():
    while True:
#        phone_input = input('Введите номер телефона: ')
        digits = ''
        for char in phone_input:
            if char.isdigit():
                digits += char
        if len(digits) >= 9:
            phone_input = '380' + digits[-9:]
        else:
            print('Неверный формат номера!')
            continue
#        print(f'Телефон "{phone_input}" записан.')
#        return phone_input

'''


if __name__ == "__main__":
    main()