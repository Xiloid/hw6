"""
    1.
    Создать файл file_practice.txt
    Записать в него строку 'Starting practice with files'
    Файл должен заканчиваться пустой строкой
"""
import re


from pathlib import Path
'''path = Path('files/file_practice.txt').resolve()
with open(path, 'w') as f:
    f.write('Starting practice with files')
    f.close()
"""
    2.
    Прочесть первые 5 символов файла и вывести содержимое в верхнем регистре
    Затем прочесть весь файл от начала до конца, вывести содержимое на экран
"""
with open(path, 'r') as f:
    f.seek(0)
    file_symbols = f.read(5)
    print(str.upper(file_symbols))
    f.seek(0)
    print(f.read())
    f.close()'''
"""
    3.
    Прочесть файл files/text.txt
    В тексте заменить все буквы 'i' на 'e', если 'i' большее кол-во,
    иначе - заменить все буквы 'e' на 'i'
    Полученный текст дописать в файл file_practice.txt
"""
path2 = Path('files/text.txt').resolve()
with open(path2, 'r+') as f:
    f.seek(0)
    all_text = f.read()
    i = all_text.count('i')
    e = all_text.count('e')
    if i > e:
        all_text = re.sub('e', 'i', all_text)
    else:
        all_text = re.sub('i', 'e', all_text)
    f.seek(0, 2)
    f.write(all_text)
    f.close()
"""
    4.
    Если в файле file_practice.txt четное количество элементов
    - файл должен заканчиваться строкой 'the end', иначе - строкой 'bye'
    Прочесть весь файл и вывести содержимое
"""

"""
    5.
    В средину файла file_practice.txt вставить строку " *some inserted text* "
    (средина - имеется в виду средина текста)
"""