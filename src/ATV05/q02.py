"""Questão 02. Calculadora de médias.

Faça um programa que:
    ○ Peça duas notas de 5 estudantes.
    ○ Calcule e armazene numa lista a média de cada estudante.
    ○ Imprima a lista de médias;
    ○ Imprima o número de estudantes com média >= 7.0.
"""

print('\n\n****\n Questão 02. Calculadora de médias\n****\n')

if __name__ == '__main__':
    medias = []
    for i in range(5):
        notas = [
            float(input(f'Informe a nota {j + 1} do estudate {i +1}: '))
            for j in range(2)
        ]
        medias.append(sum(notas) / len(notas))

    print(f'Médias: {medias}')
    print(
        f'Número de estudantes com média >= 7.0: {len([m for m in medias if m >= 7.0])}'
    )
