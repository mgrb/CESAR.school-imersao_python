"""Questão 01. Estado Civil.

Faça um algoritmo que leia a primeira letra do estado civil de uma pessoa e
mostre uma mensagem com a sua descrição (Solteiro, Casado, Viúvo, Divorciado).
Mostre uma mensagem de erro, se necessário.
"""

import sys

from communs.util import print_header

sys.path.append('/workspace/src/')


if __name__ == '__main__':
    print_header('Estado Civil')

    estado_civil = input('Digite a primeira letra do estado civil: ').upper()

    match estado_civil:
        case 'S':
            print('Solteiro')
        case 'C':
            print('Casado')
        case 'V':
            print('Viúvo')
        case 'D':
            print('Divorciado')
        case _:
            print('Estado civil inválido.')
