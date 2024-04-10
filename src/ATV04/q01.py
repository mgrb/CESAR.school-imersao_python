"""Questão 01. Contador de idades válidas.

Faça um algoritmo que leia idades até o usuário digitar -1. O programa deve
exibir o total de idades válidas digitadas, a média das idades, quantas são
maiores ou igual a 25 e quantas são menores que 25.
"""

if __name__ == '__main__':
    print('\n\n****\n contador de idades válidas \n****\n')

    # Inicializa as variáveis
    qtd_idades = 0
    qtd_idades_maior_ou_igual_25 = 0
    qtd_idades_menor_25 = 0
    soma_idades = 0
    idade = 0

    # Loop infinito
    while idade != -1:
        idade = int(input('Digite a idade: '))
        if idade < -1:
            print('Idade inválida! Digite uma idade válida.')
        elif idade != -1:
            qtd_idades += 1
            soma_idades += idade
            if idade >= 25:
                qtd_idades_maior_ou_igual_25 += 1
            else:
                qtd_idades_menor_25 += 1

print(f'Total de idades: {qtd_idades}')
print(f'Média das idades: {soma_idades / qtd_idades}')
print(f'Maiores de 25 anos: {qtd_idades_maior_ou_igual_25}')
print(f'Menores de 25 anos: {qtd_idades_menor_25}')
