"""Questão 08. Controle de estoque.

Desenvolva um programa para o controle de estoque de uma loja. O programa
deve permitir as seguintes operações:

1. Incluir produto: Permite ao usuário adicionar um produto ao estoque. O
usuário deve fornecer o nome do produto, a quantidade em estoque e o
preço unitário.
2. Excluir produto: Permite ao usuário remover um produto do estoque
usando o nome como referência.
3. Atualizar estoque: Permite ao usuário atualizar a quantidade em estoque
de um produto já existente.
4. Exibir todo o estoque: Exibe a lista de todos os produtos no estoque,
incluindo seus nomes, quantidades em estoque e preços unitários.
5. Calcular valor total do estoque: Calcula e exibe o valor total do estoque
com base nos preços dos produtos.
6. Sair: Encerra o programa.

Use um dicionário onde as chaves são os nomes dos produtos e os valores são
listas contendo a quantidade em estoque e o preço unitário.
"""

if __name__ == '__main__':
    print('\n\n****\n Questão 08. Controle de estoque \n****\n')
    estoque = {}
    while True:
        print(f'\n {"=" * 10} \n Controle de Estoque \n {"-" * 10} \n')
        print('1. Incluir produto')
        print('2. Excluir produto')
        print('3. Atualizar estoque')
        print('4. Exibir todo o estoque')
        print('5. Calcular valor total do estoque')
        print('6. Sair')

        opcao = input('Digite a opção desejada: ')

        match opcao:
            case '1':
                nome = input('Nome do produto: ')
                quantidade = int(input('Quantidade em estoque: '))
                preco = float(input('Preço unitário: '))
                estoque[nome] = [quantidade, preco]
                print(f'Produto "{nome}" adicionado ao estoque')

            case '2':
                nome = input('Nome do produto: ')
                excluido = estoque.pop(nome, None)
                print('Produto excluído') if excluido else print(
                    'Produto não encontrado',
                )

            case '3':
                nome = input('Nome do produto: ')
                quantidade = int(input('Quantidade em estoque: '))
                if nome in estoque:
                    estoque[nome][0] = quantidade
                    print(
                        f'Estoque de "{nome}" atualizado para {quantidade} unidades.',
                    )
                else:
                    print('Produto não encontrado')

            case '4':
                print('Lista de Produtos em Estoque:')
                for nome, dados in estoque.items():
                    print(f'Nome: {nome}')
                    print(f'Quantidade em Estoque: {dados[0]} unidades')
                    print(f'Preço Unitário: R$ {dados[1]:.2f}')

            case '5':
                total = sum([dados[0] * dados[1] for dados in estoque.values()])
                print(f'Valor total do estoque: R$ {total:.2f}')

            case '6':
                print('Programa finalizado.')
                break

            case _:
                print('Opção inválida')
