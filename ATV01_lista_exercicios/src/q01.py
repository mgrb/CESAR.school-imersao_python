"""Questão 1. Conversor de ângulos.

Dado um ângulo em graus, converta-o para radianos.
Utilize a fórmula: radianos = graus * pi/180.
"""

from math import pi

from communs.util import print_header

if __name__ == '__main__':
    print_header('Conversão de ângulos')
    graus = int(input('Digite o ângulo em graus: '))
    radianos = graus * pi / 180
    print(f'{graus} graus em radianos é {radianos:.2f}.')
