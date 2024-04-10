"""Questão 03. Data de nascimento.

Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário como
String. Usando manipulação de Strings, altere a frase e exiba como no exemplo.
Ex.: Você nasceu em 04 de agosto de 1970.
"""

print('\n\n****\n Questão 03. Data de nascimento\n****\n')

if __name__ == '__main__':
    data_nascimento = input('Informe a data de nascimento (dd/mm/aaaa): ')

    dia, mes, ano = data_nascimento.split('/')
    mes_extenso = [
        'janeiro',
        'fevereiro',
        'março',
        'abril',
        'maio',
        'junho',
        'julho',
        'agosto',
        'setembro',
        'outubro',
        'novembro',
        'dezembro',
    ]

    print(
        f'Você nasceu em {dia} de {mes_extenso[int(mes)-1]} de {ano}.',
    )
