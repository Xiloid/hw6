"""
    Обновите генератор паролей из hw5/password_gen.py таким образом, чтобы:
    1. Все сгенерированные пароли записывались в файл.
    2. После генерации пароля, сравнить его с содержимым файла.
        Если в файле уже записан такой пароль,
        то вывести сообщение с предупреждением "Insecure password".
    *3. Программа должна генерировать только уникальные пароли.
        Если в результате пункта 2 пароль уже содержится в файле, то генерируем
        его заново.
    * дополнительно стоит обрабатывать количество попыток генерации,
    так как после того, как будут сгенерированы все возможные комбинации,
    программа зациклится либо уйдет в бесконечную рекурсию и сломается
"""
import random
import string
import colorama
colorama.init()
from colorama import Fore, Style
from pathlib import Path
path = Path('files/passwords.txt').resolve()

def main():
    while True:
        print()
        choice = input(
            "Меню: \n"
            "1. Сгенерировать простой пароль.\n"
            "2. Сгенерировать средний пароль.\n"
            "3. Сгенерировать сложный пароль.\n"
            "4. Выход.\n"
            "Сделайте выбор и нажмите Enter: "
        )
        if choice == '1':
            pass_result, pass_length = low_pass()
            write_in_file(pass_result, pass_length)
        elif choice == '2':
            pass_result, pass_length = med_pass()
            write_in_file(pass_result, pass_length)
        elif choice == '3':
            pass_result, pass_length = strong_pass()
            write_in_file(pass_result, pass_length)
        else:
            print(Fore.GREEN + 'Выходим...', Style.RESET_ALL)
            break


def low_pass():
    pass_length = 8
    l_pass_list = random.sample(string.ascii_lowercase, pass_length)
    pass_result = ''.join(l_pass_list)
    return pass_result, pass_length


def med_pass():
    pass_length = 8
    m_pass_list = random.sample((string.ascii_letters + string.digits), pass_length)
    pass_result = ''.join(m_pass_list)
    return pass_result, pass_length


def strong_pass():
    pass_length = 16
    p_digit = p_uplet = p_downlet = p_spec = 0
    pass_result = None
    while p_digit == 0 or p_uplet == 0 or p_downlet == 0 or p_spec == 0:
        p_digit = p_uplet = p_downlet = p_spec = 0
        s_pass_res = random.sample((string.ascii_letters + string.digits + string.punctuation), pass_length)
        pass_result = ''.join(s_pass_res)
        for i in pass_result:
            if str.isdigit(i):
                p_digit += 1
            elif str.islower(i):
                p_downlet += 1
            elif str.isupper(i):
                p_uplet += 1
            else:
                p_spec += 1
    return pass_result, pass_length


def write_in_file(pass_result, pass_length):
    with open(path, 'a+') as f:
        f.seek(0)
        flag = 0
        if f.read() != '':
            f.seek(0)
            for line in f.readlines():
                new_str = line[:pass_length]
                if new_str == pass_result:
                    flag = 1
                    break
                else:
                    flag = 0
            if flag == 1:
                print(Fore.RED + 'Insecure password! Введите снова!', Style.RESET_ALL)
            else:
                f.write(pass_result + '\n')
                print(Fore.YELLOW + '===Совпадений не найдено, пароль записан===', Style.RESET_ALL)
        else:
            f.write(pass_result + '\n')
            print(Fore.YELLOW + '===Первый пароль записан===', Style.RESET_ALL)
    f.close()


if __name__ == '__main__':
    main()
