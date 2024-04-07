"""Questão 08. Calculadora de Bonos de Natal.

Uma loja deseja oferecer um bônus de natal para seus clientes. O algoritmo
deverá perguntar quantos clientes há na loja, e para cada um deles ler o nome e
o valor total das compras no ano. Se o valor for igual ou maior que R$2.000,00,
calcular um bônus de 15% e exibir “Cliente apto para receber o bônus”. Informar
ao final quantos clientes ganharam o bônus e o total em reais.
"""

from communs.util import print_header

if __name__ == '__main__':
    print_header('Calculadora de Bonos de Natal')

    qtd_clientes = int(input('Quantos clientes há na loja? '))
    total_bonos = 0.0
    qtd_clientes_com_bonos = 0

    for i in range(qtd_clientes):
        nome = input(f'Nome do {i+1}º cliente: ')
        valor_compras = float(
            input(f'Valor total das compras do {i+1}º cliente: '),
        )

        if valor_compras >= 2000.00:
            bonos = valor_compras * 0.15
            total_bonos += bonos
            qtd_clientes_com_bonos += 1
            print('Cliente apto para receber o bônus')

    print(f'Clientes {qtd_clientes_com_bonos}')
    print(f'Total R$ {total_bonos:.2f}')
