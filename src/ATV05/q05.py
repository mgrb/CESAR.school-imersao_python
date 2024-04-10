"""Questão 05. Avaliação de vendedores.

Uma loja deseja avaliar o desempenho de seus vendedores. Crie um programa que:
    ○ Solicite ao usuário o número total de vendedores da loja.
    ○ Para cada vendedor, peça ao usuário o nome do vendedor e o total de vendas
    realizadas no ano.
    ○ Determine o vendedor com o maior volume de vendas e o vendedor com o
    menor volume.
    ○ Exiba o nome de todos os vendedores e suas vendas totais, destacando o
    vendedor com as vendas mais altas e o vendedor com as vendas mais baixas.
"""

print('\n\n****\n Questão 05. Avaliação de vendedores\n****\n')

if __name__ == '__main__':
    qtd_vendedores = int(input('Informe a quantidade de vendedores: '))
    vendedores = []
    vendas = []

    for i in range(qtd_vendedores):
        vendedores.append(input(f'Informe o nome do vendedor {i + 1}: '))
        vendas.append(
            float(
                input(
                    f'Informe o total de vendas do vendedor {vendedores[i]}: ',
                ),
            ),
        )

    maior_venda = max(vendas)
    menor_venda = min(vendas)

    for i in range(qtd_vendedores):
        if vendas[i] == maior_venda:
            print(f'{vendedores[i]}: {vendas[i]} - Maior volume de vendas!')
        elif vendas[i] == menor_venda:
            print(f'{vendedores[i]}: {vendas[i]} - Menor volume de vendas!')
        else:
            print(f'{vendedores[i]}: {vendas[i]}')
