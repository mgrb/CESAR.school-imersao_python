"""Questão 06. Sync de Dicionários.

Escreva um programa que faça a atualização no dicionário numeros_maria de
acordo com os valores de numeros_sara. Porém, ele não deve adicionar novos
valores, só atualizar os existentes. Os dicionários já estão definidos, não é
necessário requerer informações do usuário. São eles:

● numeros_maria = {'a': 100, 'b': 200, 'c': 300}
● numeros_sara = {'a': 300, 'b': 200, 'd': 400, 'c': 500, 'e': 250}.
"""

if __name__ == '__main__':
    print('\n\n****\n Questão 06. Sync de Dicionários\n****\n')

    numeros_maria = {'a': 100, 'b': 200, 'c': 300}
    numeros_sara = {'a': 300, 'b': 200, 'd': 400, 'c': 500, 'e': 250}

    for key in numeros_sara:
        if key in numeros_maria:
            numeros_maria[key] = numeros_sara[key]

    print(numeros_maria)
