"""Questão 02. Avaliação de Produtos.

Uma loja online deseja criar um sistema de avaliação de produtos. O usuário deve
inserir uma nota de 1 a 5 para um produto. Se uma nota inválida for digitada o
usuário deverá ser alertado. O programa deve calcular a média das notas.
Continue coletando notas até que o usuário insira -1.
"""

if __name__ == '__main__':
    print('\n\n****\n Avaliação de Produtos \n****\n')

    # Inicializa as variáveis
    qtd_notas: int = 0
    soma_notas: int = 0
    nota: int = 0.0

    # Loop infinito
    while nota != -1:
        nota = int(input('Digite a nota do produto (1 a 5): '))
        if nota < 1 or nota > 5:
            print('Nota inválida!')
        elif nota != -1:
            qtd_notas += 1
            soma_notas += nota

    print(f'Média das notas: {soma_notas / qtd_notas}')
