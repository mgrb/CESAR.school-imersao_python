"""Questão 2. Cauculadora de desconto.

Peça ao usuário para inserir o valor original de um produto e a porcentagem de
desconto. Calcule e mostre o valor do produto após o desconto.
"""

from communs.util import print_header

if __name__ == '__main__':
    print_header('Calculadora de desconto')
    valor_original = float(input('Digite o valor original do produto: '))
    desconto = float(input('Digite a porcentagem de desconto: '))
    valor_descontado = valor_original * (1 - desconto / 100)
    print(f'Valor com desconto: R$ {valor_descontado:.2f}.')
