"""Questão 01. Paleta de cores - RGB.

Crie um programa que contenha uma lista de tuplas, onde cada tupla contém o
nome de uma cor e seus valores RGB (Red, Green, Blue), informadas pelo
usuário. Para inserir os valores, o sistema deverá solicitar quantas cores o
usuário deseja informar. Após a inserção, solicite ao usuário que digite o nome
de uma cor e, se a cor estiver na lista, exiba seus valores RGB.

Lista de Tupla = cores_rgb[(nome_da_cor, (r,g,b) ), (nome_da_cor, (r,g,b) )].
"""

if __name__ == '__main__':
    print('\n\n****\n Paleta de cores - RGB \n****\n')

    cores_rgb = []
    qtd_cores = int(input('Quantas cores deseja informar? '))
    for i in range(qtd_cores):
        nome_cor = input('Nome da cor: ')
        r = int(input('Valor de RED: '))
        g = int(input('Valor de GREEN: '))
        b = int(input('Valor de BLUE: '))
        cores_rgb.append((nome_cor.lower(), (r, g, b)))

    cor = input('Digite o nome da cor: ')
    for c in cores_rgb:
        if cor.lower() == c[0]:
            print(
                f'Valores RGB para a cor {c[0].title()}: Red={c[1][0]}, Green={c[1][1]}, Blue={c[1][2]}',
            )
            break
    else:
        print('Cor não encontrada.')
