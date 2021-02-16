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
    with open(in_path, 'r') as f:
        counter = 1
        for line in f.readlines():
            in_name = re.findall(r'[a-zA-Z]', line)
            in_phone = re.findall(r'\d', line)
            out_name = ''.join(in_name)
            out_phone = ''.join(in_phone)
            n_capitalized = out_name.capitalize()
            if n_capitalized.find('M') == 0 or n_capitalized.rfind('a') == len(n_capitalized) - 1:
                good_phone = phone_func(out_phone)
                whole_string = str(counter) + '. ' + good_phone + ' - ' + n_capitalized
                counter += 1
                write_func(whole_string)
        print('Телефонная книга отформатирована.')
        f.close()


def write_func(name):
    with open(out_path, 'a') as f:
        print(name, file=f)
        f.close()


def phone_func(phone):
    digits = ''
    for char in phone:
        if char.isdigit():
            digits += char
    if len(digits) >= 9:
        phone = '+380' + digits[-9:]
        return phone


if __name__ == "__main__":
    main()