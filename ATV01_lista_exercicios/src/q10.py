"""Questão 10. Calculadora de crediário.

Peça ao usuário para inserir o valor total de uma compra e o número de parcelas
desejadas. Calcule e mostre o valor de cada parcela, considerando que não há
juros.
"""

from communs.util import print_header

if __name__ == '__main__':
    print_header('Calculadora de Crediário')
    valor_total = float(input('Digite o valor total da compra: '))
    numero_parcelas = int(input('Digite o número de parcelas: '))
    valor_parcela = valor_total / numero_parcelas
    print(
        f'Valor de cada parcela: R$ {valor_parcela:.1f}',
    )  # TODO(Sugestão): 1f -> 2f
