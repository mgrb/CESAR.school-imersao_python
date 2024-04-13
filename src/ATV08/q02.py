"""Questão 02. Campeonato de Kart.

Uma pista de Kart permite 3 voltas para cada um dos 4 corredores. No
programa principal, implemente um código que leia o nome do corredor e todos
os tempos em segundos e os guarde em um dicionário, onde a chave é o nome
do corredor. Implemente duas funções:

1. Uma função chamada calcular_media que recebe uma lista de tempos
como parâmetro e retorna a média desses tempos.
2. Uma função chamada encontrar_campeao que recebe o dicionário de
tempos como parâmetro e usa a função calcular_media para calcular a
média de tempo de cada corredor. A função deve identificar o campeão
(corredor com a menor média de tempo) e retornar o nome do campeão
e sua média de tempo com duas casas decimais (use
round(menor_media, 2).

No final do programa principal, exiba o nome do campeão em maiúsculas e sua
média de tempo com duas casas decimais.
"""

from __future__ import annotations


def calcular_media(tempos: list) -> float:
    """Função que calcula a média dos tempos.

    Arguments:
    ---------
        tempos: {list}  Lista com os tempos em segundos.

    Returns:
    -------
        float: Média dos tempos.

    """
    return sum(tempos) / len(tempos)


def encontrar_campeao(tempos_dict: dict) -> tuple[str, float]:
    """Função que encontra o campeão.

    Arguments:
    ---------
        tempos_dict: {dict}  Dicionário com os tempos dos corredores.

    Returns:
    -------
        tuple[str, float]: Nome do campeão e sua média de tempo.

    """
    menor_media = float('inf')
    campeao = ''
    for corredor, tempos in tempos_dict.items():
        media = calcular_media(tempos)
        if media < menor_media:
            menor_media = media
            campeao = corredor

    return campeao, round(menor_media, 2)


def main() -> None:
    """Função principal."""
    print('Campeonato de Kart')

    tempos = {}
    for i in range(4):
        corredor = input('Digite o nome do corredor: ')
        tempos[corredor] = [
            float(input(f'Digite o tempo da volta {j + 1}: ')) for j in range(3)
        ]

    campeao, media = encontrar_campeao(tempos)
    print(
        f'O campeão é {campeao.upper()} com média de tempo de {media} segundos.',
    )


if __name__ == '__main__':
    main()
