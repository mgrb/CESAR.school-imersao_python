"""Questão 3. Caucule a área de um triângulo - Heron.

Dados os lados a, b, e c de um triângulo, calcule sua área.
Utilize a fórmula de Heron:
"""

from communs.util import print_header


def calc_semiperimetro(a: float, b: float, c: float) -> float:
    """Calcula o semiperímetro de um triângulo."""
    return (a + b + c) / 2


def calc_area_heron(a: float, b: float, c: float) -> float:
    """Calcula a área de um triângulo utilizando a fórmula de Heron."""
    s = calc_semiperimetro(a, b, c)
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


if __name__ == '__main__':
    print_header('Área de um triângulo - Heron')
    a = float(input('Digite o tamanho do lado a: '))
    b = float(input('Digite o tamanho do lado b: '))
    c = float(input('Digite o tamanho do lado c: '))

    area = calc_area_heron(a, b, c)
    print(f'Área do triângulo: {area:.1f}')
