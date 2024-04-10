"""Questão 09. Análise de Vendas.

Uma grande rede de lojas deseja analisar o desempenho de vendas de seus rodutos
ao longo de um ano. Para isso, eles coletaram os valores de vendas mensais de
um determinado produto durante os 12 meses do ano. O sistema deve permitir que
o usuário insira os valores de vendas para cada mês, começando por janeiro e
terminando em dezembro. Após a inserção, o programa deve calcular:

● O mês com a maior venda.
● O mês com a menor venda.
● A média de vendas ao longo do ano.
● O total de vendas no ano.
"""

if __name__ == '__main__':
    print('\n\n****\n Análise de Vendas \n****\n')

    mes_maior_venda = None
    mes_menor_venda = None

    total_maior_venda: float = 0.0
    total_menor_venda: float = 0.0

    total_vendas: float = 0.0
    media_vendas: float = 0.0

    for i in range(12):
        vendas_mes = float(input(f'Vendas do {i+1}º mês: '))

        total_maior_venda = vendas_mes if i == 0 else total_maior_venda
        total_menor_venda = vendas_mes if i == 0 else total_menor_venda

        if vendas_mes >= total_maior_venda:
            total_maior_venda = vendas_mes
            mes_maior_venda = i + 1

        if vendas_mes <= total_menor_venda:
            total_menor_venda = vendas_mes
            mes_menor_venda = i + 1

        total_vendas += vendas_mes

    media_vendas = total_vendas / 12

    match mes_maior_venda:
        case 1:
            mes_maior_venda = 'Janeiro'
        case 2:
            mes_maior_venda = 'Fevereiro'
        case 3:
            mes_maior_venda = 'Março'
        case 4:
            mes_maior_venda = 'Abril'
        case 5:
            mes_maior_venda = 'Maio'
        case 6:
            mes_maior_venda = 'Junho'
        case 7:
            mes_maior_venda = 'Julho'
        case 8:
            mes_maior_venda = 'Agosto'
        case 9:
            mes_maior_venda = 'Setembro'
        case 10:
            mes_maior_venda = 'Outubro'
        case 11:
            mes_maior_venda = 'Novembro'
        case 12:
            mes_maior_venda = 'Dezembro'

    match mes_menor_venda:
        case 1:
            mes_menor_venda = 'Janeiro'
        case 2:
            mes_menor_venda = 'Fevereiro'
        case 3:
            mes_menor_venda = 'Março'
        case 4:
            mes_menor_venda = 'Abril'
        case 5:
            mes_menor_venda = 'Maio'
        case 6:
            mes_menor_venda = 'Junho'
        case 7:
            mes_menor_venda = 'Julho'
        case 8:
            mes_menor_venda = 'Agosto'
        case 9:
            mes_menor_venda = 'Setembro'
        case 10:
            mes_menor_venda = 'Outubro'
        case 11:
            mes_menor_venda = 'Novembro'
        case 12:
            mes_menor_venda = 'Dezembro'

    print(
        f'Mês com a maior venda: {mes_maior_venda} (R$ {total_maior_venda:.2f})',
    )
    print(
        f'Mês com a menor venda: {mes_menor_venda} (R$ {total_menor_venda:.2f})',
    )
    print(f'MMédia de vendas ao longo do ano: R$ {media_vendas:.2f}')
    print(f'Total de vendas no ano: R$ {total_vendas:.2f}')
