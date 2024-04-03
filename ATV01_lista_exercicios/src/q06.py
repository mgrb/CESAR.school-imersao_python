"""Questão 6. Calculadora de área de círculo.

Dado um raio r e calcule e mostre a área de um círculo.
"""

from math import pi

from communs.util import print_header

if __name__ == '__main__':
    print_header('Calculadora de área de círculo')
    raio = float(input('Digite o raio do círculo: '))
    area = pi * raio**2
    print(f'Área do círculo: {area:.1f}.')
