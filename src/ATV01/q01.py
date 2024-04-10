"""Questão 1. Conversor de ângulos.

Dado um ângulo em graus, converta-o para radianos.
Utilize a fórmula: radianos = graus * pi/180.
"""

from math import pi

if __name__ == '__main__':
    print('\n\n****\n Conversão de ângulos \n****\n')
    graus = int(input('Digite o ângulo em graus: '))
    radianos = graus * pi / 180
    print(f'{graus} graus em radianos é {radianos:.2f}.')
