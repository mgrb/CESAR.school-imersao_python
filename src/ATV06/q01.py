"""Questão 01. E-mail válido.

Faça um programa que receba um e-mail e verifique se ele é válido. Obs: Para um
e-mail ser válido considerar se possui “@”.
"""

print('\n\n****\n Questão 01. E-mail válido\n****\n')

if __name__ == '__main__':
    email = input('Informe o e-mail: ')

    if '@' in email:
        print('E-mail válido.')
    else:
        print('E-mail inválido.')
