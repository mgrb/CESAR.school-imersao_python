"""Questão 04: Classificador de Motoristas.

Em uma cidade, a prefeitura deseja classificar os motoristas com base em suas
infrações de trânsito no último ano. O objetivo é criar um programa de
reeducação para os motoristas que cometem infrações. Para isso, eles definiram
as seguintes categorias:

a) Motorista Exemplar: Não cometeu nenhuma infração.
b) Motorista Atento: Cometeu até 3 infrações.
c) Motorista Desatento: Cometeu entre 4 e 6 infrações.
d) Motorista Perigoso: Cometeu mais de 6 infrações.

Escreva um programa que peça ao usuário para inserir o número de infrações que
cometeu no último ano e informe em qual categoria ele se encaixa.
"""

from communs.util import print_header

if __name__ == '__main__':
    print_header('Classificador de Motoristas')

    num_infracoes = int(
        input('Digite o número de infrações cometidas no último ano: '),
    )

    classificacao: str = None

    if num_infracoes == 0:
        classificacao = 'Motorista Exemplar'
    elif num_infracoes <= 3:
        classificacao = 'Motorista Atento'
    elif 4 <= num_infracoes <= 6:
        classificacao = 'Motorista Desatento'
    else:
        classificacao = 'Motorista Perigoso'

    print(f'Categoria: {classificacao}')
