"""Questão 04. Dicionário de Quadrados.

Faça um programa que crie um dicionário onde as chaves serão os números de 1
a 15 e os valores serão o quadrado desses números.
"""

if __name__ == '__main__':
    print('\n\n****\n Questão 04. Dicionário de Quadrados\n****\n')

    dicionario = {i: i**2 for i in range(1, 16)}

    print(dicionario)
