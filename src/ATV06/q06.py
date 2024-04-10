"""Questão 06. Média de estudantes.

Faça um programa que leia o nome e três notas de 3 estudantes. Os nomes e as
médias devem ser armazenadas, cada um, em uma lista. Por fim, em outra
estrutura de repetição, exiba o nome e a média, um a um, formatando o nome para
ser exibido com a primeira letra maiúscula e o restante minúscula e a média
para apenas duas casas decimais. Informe também se o estudante está aprovado ou
reprovado. Obs: Para ser aprovado a média deve ser maior ou igual a 7.
"""

print('\n\n****\n Questão 06. Média de estudantes\n****\n')

if __name__ == '__main__':
    estudantes = []
    for i in range(3):
        nome = input('Informe o nome do estudante: ')
        notas = []
        for j in range(3):
            nota = float(input(f'Informe a {j + 1}ª nota: '))
            notas.append(nota)
        estudantes.append([nome, notas])

    for estudante in estudantes:
        nome = estudante[0].capitalize()
        media = sum(estudante[1]) / len(estudante[1])
        status = 'aprovado' if media >= 7 else 'reprovado'
        print(
            f'A média de {nome} é {media:.2f} e ele(a) esta {status}',
        )
