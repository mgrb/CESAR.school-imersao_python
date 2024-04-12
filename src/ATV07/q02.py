"""Questão 02. Calculadora Euclidiana.

Crie um programa que leia as coordenadas x, y e z de dois pontos no espaço 3D,
representados como tuplas. Calcule a distância entre esses dois pontos usando a
fórmula da distância Euclidiana:

𝑑 = ((𝑥2 − 𝑥1)^2 + (𝑦2 − 𝑦1)^2 + (𝑧2 − 𝑧1)^2)^0.5

Exiba a distância calculada.
"""

if __name__ == '__main__':
    print('\n\n****\n Questão 02. Calculadora Euclidiana\n****\n')

    p1 = tuple(
        map(
            float,
            input('Informe as coordenadas do primeiro ponto (x, y, z): ').split(
                ',',
            ),
        ),
    )
    p2 = tuple(
        map(
            float,
            input('Informe as coordenadas do segundo ponto (x, y, z): ').split(
                ',',
            ),
        ),
    )

    d = (
        (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2
    ) ** 0.5

    print(f'A distância entre os pontos é: {d:.2f}')
