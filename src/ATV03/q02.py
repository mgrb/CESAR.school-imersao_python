"""Questão 02. Calculadora de Aumento Salarial.

Escreva um algoritmo que receba o código correspondente ao cargo de um
funcionário de uma escola e seu salário atual. Mostre o valor do novo salário,
com aumento, conforme tabela abaixo:
"""

import sys

from communs.util import print_header

if __name__ == '__main__':
    print_header('Calculadora de Aumento Salarial')

    cargo: int = int(input('Digite o código do cargo: '))
    salario: float = float(input('Digite o salário atual: '))

    match cargo:
        case 1:  # Secretário
            novo_salario = salario * 1.45
        case 2:  # Tesoureiro
            novo_salario = salario * 1.35
        case 3:  # Professor
            novo_salario = salario * 1.25
        case 4:  # Coordenador
            novo_salario = salario * 1.15
        case 5:  # Diretor
            novo_salario = salario * 1
        case _:
            print('Cargo inválido.')
            sys.exit()

    print(f'Salário atualizado: R$ {novo_salario:.2f}')
