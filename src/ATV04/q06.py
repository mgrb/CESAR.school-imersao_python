"""Questão 06. Maior numero par.

Faça um algoritmo que encontre qual o maior número par digitado pelo usuário. O
usuário deve digitar 10 números e ao final o algoritmo deve imprimir o
resultado.
Faça também um algoritmo que encontre qual o menor número par digitado pelo 
usuário.
"""

from communs.util import print_header

if __name__ == '__main__':
    print_header('Maior número par')

    maior: int = None
    menor: int = None

    for i in range(10):
        num = int(input(f'Digite o {i+1}º número: '))
        if num % 2 == 0:
            if maior is None or num > maior:
                maior = num
            if menor is None or num < menor:
                menor = num


    print(f'Maior número par: {maior}.')
    print(f'Menor número par: {menor}.')