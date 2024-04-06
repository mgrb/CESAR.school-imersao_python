"""Questão 06: PDV Ingressos.

Uma rede de cinemas deseja criar um sistema para controlar a venda de ingressos.
Eles possuem três tipos de sessões: Matinê, Vespertina e Noturna. Cada sessão
tem um preço diferente. As regras são:

1. Sessão Matinê: Custa R$ 20.
2. Sessão Vespertina: Custa R$ 25.
3. Sessão Noturna: Custa R$ 30.

Crianças até 12 anos, estudantes e idosos (65+) têm direito a 50% de desconto em
qualquer sessão. Escreva um programa que peça ao usuário para escolher o tipo de
sessão e informar a idade. Caso o usuário não seja idoso ou criança, ele deverá
informar se é estudante. O programa deve informar o valor total da compra.
"""

from communs.util import print_header

if __name__ == '__main__':
    print_header('PDV Ingressos')

    tipo_sessao = int(
        input('Escolha o tipo de sessão (1-Matinê, 2-Vespertina, 3-Noturna): '),
    )

    idade = int(input('Digite a idade: '))
    is_estudante = (
        12 < idade < 65 and input('É estudante? (S/N): ').upper() == 'S'
    )

    valor_total: float = 0

    match tipo_sessao:
        case 1:
            valor_total = 20
        case 2:
            valor_total = 25
        case 3:
            valor_total = 30
        case _:
            print('Tipo de sessão inválido.')

    if idade <= 12 or idade >= 65 or is_estudante:
        valor_total *= 0.5

    print(f'Valor do ingresso: R$ {valor_total:.2f}')
