"""Questão 7. Calculadora de custo vs lucro.

Escreva um programa que leia o custo de produção de um produto e seu preço de
venda. Calcule e mostre o lucro bruto obtido na venda do produto.
"""

if __name__ == '__main__':
    print('\n\n****\n Calculadora de Custo vs Lucro \n****\n')
    custo_producao = float(input('Digite o custo de produção: '))
    preco_venda = float(input('Digite o preço de venda: '))
    lucro_bruto = preco_venda - custo_producao
    print(f'Lucro Bruto: R$ {lucro_bruto:.1f}')  # TODO(Sugestão): 1f -> 2f
