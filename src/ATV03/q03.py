"""Questão 03: Dia da Semana.

Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-
Domingo, 2- Segunda, etc.). Exibir mensagem “Valor Inválido” caso um número
inesperado for informado.
"""

from communs.util import print_header

if __name__ == '__main__':
    print_header('Dia da Semana')

    dia = int(input('Digite o número correspondente ao dia da semana: '))

    match dia:
        case 1:
            print('Domingo')
        case 2:
            print('Segunda')
        case 3:
            print('Terça')
        case 4:
            print('Quarta')
        case 5:
            print('Quinta')
        case 6:
            print('Sexta')
        case 7:
            print('Sábado')
        case _:
            print('Valor Inválido')
