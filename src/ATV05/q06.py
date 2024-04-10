"""Questão 06. Avaliação de restaurantes.

Desenvolva um programa que permita aos usuários avaliarem restaurantes com
notas de 0 a 5. Cada restaurante só deve ser inserido uma vez na lista. Se um
restaurante for avaliado mais de uma vez, o programa deve atualizar a nota
média do restaurante considerando todas as avaliações fornecidas até o momento,
mas o restaurante não deve ser adicionado novamente à lista.

O programa deve:

    ● Solicitar o nome do restaurante ou digitar “PARE” para finalizar.
    ● Solicitar a nota dada pelo usuário (de 0 a 5).
    ● Se o restaurante já foi avaliado anteriormente, atualizar a nota média
    considerando todas as avaliações anteriores e a nova avaliação. Use a
    seguinte fórmula: nova média = (média anterior x número de avaliações +
    nova nota) / (número de avaliações + 1)

Ao final, o programa deve mostrar o restaurante com a maior nota média e o
restaurante com a menor nota média.
"""

print('\n\n****\n Questão 06. Avaliação de Restaurantes\n****\n')

if __name__ == '__main__':
    restaurantes = []
    avaliacoes = []

    restaurante = None

    while restaurante != 'PARE':
        restaurante = input(
            'Informe o nome do restaurante ou digite "PARE" para finalizar: ',
        )

        if restaurante == 'PARE':
            break

        nota = float(input('Informe a nota do restaurante (de 0 a 5): '))

        restaurantes.append(restaurante)
        avaliacoes.append(nota)

    # TODO: Implementar a lógica de atualização da média de avaliações
