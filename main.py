from random import randint
from sys import exit

from numpy import base_repr


def input_password():
    # function for input password and translate number system
    try:
        login = input("login:")
        password = input("Password🔑:")
        password = int(password, 36)

    except ValueError:
        print("введите другое значение")
        input_password()
    encrypt(password, login)


def encrypt(password, login):
    # function create original key for encrypt password and encrypt
    key = randint(1, 100000)
    try:
        encryption = key ^ password
        print("# пароль зашиврован #")

        save_password(encryption, key, login)
        what_to_do(key, encryption, login)
    except TypeError:
        input_password()


def what_to_do(key, encryption, login):
    # function doing action
    action = input("что хотите сделать?"
                   "\n1.посмотреть записанный пароль"
                   "\n2.записать пароль"
                   "\n3.посмотреть предыдущий пароль"
                   "\n4.выйти\n")

    if (action in "посмотреть пароль" or action in "1"):
        decrypt(key, encryption, login)

    elif (action in "записать пароль" or action in "2"):
        input_password()

    elif (action in "выйти" or action in"4"):
        exit()

    elif (action in "посмотреть предыдущий пароль" or action in "3"):
        read_password(key, encryption, login)
        # countdown starts from zero

    else:
        print("не понял запрос")
        what_to_do(key, encryption, login)


def save_password(encryption, key, login):
    # function save password, keys and login in txt file
    with open('password.txt', 'a') as file:
        file.write(f"{encryption}\n")

    with open('key.txt', 'a') as file:
        file.write(f"{str(key)}\n")

    with open('login.txt', 'a') as file:
        file.write(f"{str(login)}\n")


def read_password(key, encryption, login):
    # function takes from file encryption, key
    # and login for show password

    with open('login.txt', 'r') as file:
        for index, lines in enumerate(file):
            print(f'{index}.{lines}')

    num = int(input("какой пароль вывести?"))

    with open('password.txt', 'r') as file:
        for index, line in enumerate(file):
            if index == num:
                encryption = line
                encryption = int(encryption)
                break

    with open('key.txt', 'r') as file:
        for index, line in enumerate(file):
            if index == num:
                key = line
                key = int(key)
                break

    decrypt(key, encryption, login)


def decrypt(key, encryption, login):
    # function decrypt password
    # and translate in 36 number system

    password = key ^ encryption
    password = base_repr(password, 36)

    print(f"Password🔑: {password}")
    what_to_do(key, encryption, login)


if __name__ == "__main__":
    while True:
        input_password()
