#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

import os
os.system("cls")

user = "zampieri"
key = 135


def pedir_dados():
    user_input = input('\nDigite seu usuário: ')
    key_input = int(input('\nDigite sua senha: '))
    login(user_input, key_input)


def login(user_input, key_input):
    if user_input == user and key_input == key:
        print('\nUsuário e senhas corretos!\n')
        print('Seja bem vindo/a!\n')
    else:
        print('\nUsuário ou senha incorretos!')
        pedir_dados()


pedir_dados()