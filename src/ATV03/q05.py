"""Questão 05: Sistema de Reservas.

Um hotel de luxo deseja automatizar seu sistema de reservas. Eles possuem três
tipos de suítes: Standard, Luxo e Presidencial. Cada tipo de suíte tem uma
quantidade limitada de noites que pode ser reservada a um preço diferente. O
hotel definiu as seguintes regras:

1. Suíte Standard: Custa R$ 250 por noite, limite de 15 noites.
2. Suíte Luxo: Custa R$ 500 por noite, limite de 10 noites.
3. Suíte Presidencial: Custa R$ 1200 por noite, limite de 7 noites.

Além disso, se o cliente desejar ficar 5 noites ou mais, ele recebe um desconto
de 10% no valor total, independentemente do tipo de suíte escolhida. Escreva um
programa que peça ao usuário para escolher o tipo de suíte, a quantidade de
noites e informe o valor total da estadia. Se a quantidade de noites informada
for maior que o limite disponível, informe ao usuário e finalize o sistema.
"""

from communs.util import print_header

if __name__ == '__main__':
    print_header('Sistema de Reservas')

    tipo_suite = int(
        input('Escolha o tipo de suíte (1-Standard, 2-Luxo, 3-Presidencial): '),
    )

    num_noites = int(input('Digite a quantidade de noites: '))

    valor_total: float = 0
    is_out_of_limit = False

    match tipo_suite:
        case 1:
            is_out_of_limit = num_noites > 15
            valor_total = num_noites * 250
        case 2:
            is_out_of_limit = num_noites > 10
            valor_total = num_noites * 500
        case 3:
            is_out_of_limit = num_noites > 7
            valor_total = num_noites * 1200
        case _:
            print('Tipo de suíte inválido.')

    if num_noites >= 5:
        valor_total *= 0.9

    if is_out_of_limit:
        print('Limite de noites atingido.')
    else:
        print(f'Valor total da estadia: R$ {valor_total:.2f}')
