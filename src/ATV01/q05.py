"""Questão 5. Calculadora de Comissão.

Escreva um programa que leia o valor total das vendas de um vendedor e a
porcentagem de comissão que ele recebe. Calcule e mostre o valor da comissão.
"""

if __name__ == '__main__':
    print('\n\n****\n Calculadora de Comissão \n****\n')
    valor_vendas = float(input('Digite o valor total das vendas: '))
    comissao = float(input('Digite a porcentagem de comissão: '))
    valor_comissao = valor_vendas * comissao / 100
    print(f'Valor da comissão: R$ {valor_comissao:.2f}')
