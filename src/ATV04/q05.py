"""Questão 05. Avaliação de altura.

Faça um programa que leia o nome, idade e altura de 5 pessoas. O sistema deverá
apresentar o nome, idade e altura da pessoa mais alta.
"""

QTD_PESSOAS = 5

if __name__ == '__main__':
    print('\n\n****\n Pessoa mais alta \n****\n')

    nome_maior: str = ''
    idade_maior: int = 0
    altura_maior: float = 0.0

    for i in range(QTD_PESSOAS):
        nome = input(f'Nome da {i+1}ª pessoa: ')
        idade = int(input(f'Idade da {i+1}ª pessoa: '))
        altura = float(input(f'Altura da {i+1}ª pessoa: '))

        if i == 0:
            altura_maior = altura
            nome_maior = nome
            idade_maior = idade
        if altura > altura_maior:
            altura_maior = altura
            nome_maior = nome
            idade_maior = idade

    print(
        f'{nome_maior}, com {idade_maior} anos e {altura_maior}m, é a pessoa mais alta do grupo.',
    )
