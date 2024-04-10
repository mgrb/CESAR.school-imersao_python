"""Questão 03. Separador de números.

Faça um programa em duas partes:
    ○ Parte 01: Ler 10 números inteiros e armazená-los em uma lista única.
    ○ Parte 02: Em uma nova estrutura de repetição, armazene os números pares na
    lista PARES e os números ímpares na lista ÍMPARES.
    ○ Imprima as três listas.
"""

print('\n\n****\n Questão 03. Separador de Numeros \n****\n')

if __name__ == '__main__':
    numeros = [int(input(f'Informe o número {i + 1}: ')) for i in range(10)]
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]

    print(f'Números: {numeros}')
    print(f'Pares: {pares}')
    print(f'Ímpares: {impares}')
