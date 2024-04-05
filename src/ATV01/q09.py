"""Questão 9. Calculadora de custo fiscal.

Peça ao usuário para inserir o valor de um produto e a taxa de imposto aplicada
sobre ele. Calcule e mostre o valor final do produto com o imposto.
"""

from communs.util import print_header

if __name__ == '__main__':
    print_header('Calculadora de Custo Fiscal')
    valor_produto = float(input('Digite o valor do produto: '))
    taxa_imposto = float(input('Digite a taxa de imposto: '))
    valor_final = valor_produto * (1 + taxa_imposto / 100)
    print(
        f'Valor Final com Imposto: R$ {valor_final:.1f}',
    )  # TODO(Sugestão): 1f -> 2f
