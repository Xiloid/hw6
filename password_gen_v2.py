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
            low_pass()
        elif choice == '2':
            med_pass()
        elif choice == '3':
            strong_pass()
        else:
            print('Выходим...')
            break


def low_pass():
    l_pass_list = random.sample(string.ascii_lowercase, 8)
    print('Ваш пароль:', ''.join(l_pass_list))


def med_pass():
    m_pass_list = random.sample((string.ascii_letters + string.digits), 8)
    print('Ваш пароль:', ''.join(m_pass_list))


def strong_pass():
    p_digit = p_uplet = p_downlet = p_spec = 0
    pass_string = None
    while p_digit == 0 or p_uplet == 0 or p_downlet == 0 or p_spec == 0:
        p_digit = p_uplet = p_downlet = p_spec = 0
        s_pass_length = random.randint(8, 16)
        s_pass_res = random.sample((string.ascii_letters + string.digits + string.punctuation), s_pass_length)
        pass_string = ''.join(s_pass_res)
        for i in pass_string:
            if str.isdigit(i):
                p_digit += 1
            elif str.islower(i):
                p_downlet += 1
            elif str.isupper(i):
                p_uplet += 1
            else:
                p_spec += 1
    print('Ваш пароль:', pass_string)


if __name__ == '__main__':
    main()