"""Questão 01. Calculadora de faixas etárias.

Faça um programa que leia um número indeterminado de valores, correspondentes a
idades, encerrando a entrada de dados quando for informado um valor igual a -1
que não deve ser armazenado). Após esta entrada de dados, faça:

    ○ Mostre a quantidade de idades válidas;
    ○ Exiba as idades armazenadas;
    ○ Calcule e mostre a média das idades;
    ○ Calcule e mostre a quantidade de idades acima da média calculada;
    ○ Exiba a maior e menor idade;
    ○ Calcule e mostre a quantidade de valores abaixo de 18.
"""

print('\n\n****\n Questão 01. Calculadora de faixas etárias\n****\n')

if __name__ == '__main__':
    idade = 0
    idades = []
    while idade != -1:
        idade = int(input('Informe a idade: '))
        if idade != -1:
            idades.append(idade)

    print(f'Quantidade de idades válidas: {len(idades)}')
    print(f'Idades armazenadas: {idades}')
    print(f'Média das idades: {sum(idades) / len(idades)}')
    print(
        f'Quant. de idades acima da média: {len([i for i in idades if i > sum(idades) / len(idades)])}',
    )
    print(f'Maior idade: {max(idades)}')
    print(f'Menor idade: {min(idades)}')
    print(
        f'Quant. de idades abaixo de 18: {len([i for i in idades if i < 18])}',
    )
