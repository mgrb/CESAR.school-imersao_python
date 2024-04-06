"""Questão 06. Maior numero par.

Faça um algoritmo que encontre qual o maior número par digitado pelo usuário. O
usuário deve digitar 10 números e ao final o algoritmo deve imprimir o
resultado.
"""

from communs.util import print_header

if __name__ == '__main__':
    print_header('Maior número par')

    maior: int = 0

    for i in range(10):
        num = int(input(f'Digite o {i+1}º número: '))

        if num % 2 == 0 and num > maior:
            maior = num

    print(f'Maior número par: {maior}.')
