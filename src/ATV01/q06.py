"""Questão 6. Calculadora de área de círculo.

Dado um raio r e calcule e mostre a área de um círculo.
"""

from math import pi

if __name__ == '__main__':
    print('\n\n****\n Calculadora de área de círculo \n****\n')
    raio = float(input('Digite o raio do círculo: '))
    area = pi * raio**2
    print(f'Área do círculo: {area:.1f}.')
