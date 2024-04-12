"""Questão 05. Kartodromo.

Uma pista de Kart permite 3 voltas para cada um dos 4 corredores. Escreva um
programa que leia todos os tempos em segundos e os guarde em um dicionário,
onde a chave é o nome do corredor. Ao final diga quem foi o campeão,
apresentando o nome (com a todas as letras maiúsculas) e sua média de tempo
(com duas casas decimais). Lembre-se: o campeão tem a menor média.
"""

if __name__ == '__main__':
    print('\n\n****\n Kartodromo \n****\n')

    tempos = {}
    for i in range(4):
        corredor = input('Nome do corredor: ')
        tempos[corredor.upper()] = []
        for v in range(3):
            tempo = float(input(f'Tempo da volta {v+1} (s): '))
            tempos[corredor.upper()].append(tempo)

    campeao = ''
    menor_media = 0
    for corredor, tempos in tempos.items():
        media = sum(tempos) / len(tempos)
        if not menor_media or media < menor_media:
            menor_media = media
            campeao = corredor

    print(
        f'O campeão foi {campeao} com média de {menor_media:.2f} segundos.',
    )
