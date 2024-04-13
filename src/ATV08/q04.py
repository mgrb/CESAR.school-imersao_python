"""Questão 04. Atualização de dicionário.

Escreva no programa principal um bloco de códigos que atualize o dicionário
numeros_maria com base nos valores do dicionário numeros_sara. A atualização
deve ser feita apenas nos valores já existentes no dicionário numeros_maria.
Não é necessário adicionar novos valores. Os dicionários já estão definidos
como segue:

● numeros_maria = {'a': 100, 'b': 200, 'c': 300}
● numeros_sara = {'a': 300, 'b': 200, 'd': 400, 'c': 500, 'e': 250}

Crie uma função chamada atualizar_numeros que recebe os dois dicionários
como parâmetros e atualiza o dicionário numeros_maria de acordo com os
valores do dicionário numeros_sara. Os valores no dicionário numeros_maria
devem ser substituídos pelos valores correspondentes do dicionário
numeros_sara se a chave existir em ambos os dicionários. A função não irá
retornar nenhum valor. Irá imprimir o dicionário numeros_maria atualizado.
"""


def atualizar_numeros(update_target: dict, origin: dict) -> None:
    """Função que atualiza os valores do dicionário maria com base no dicionário sara.

    Arguments:
    ---------
        update_target: {dict}  Dicionário a ser atualizado.
        origin: {dict}  Dicionário com os novos valores.

    """
    for chave, valor in origin.items():
        if chave in update_target:
            update_target[chave] = valor


def main() -> None:
    """Função principal."""
    print('Atualização de Dicionário')

    numeros_maria = {'a': 100, 'b': 200, 'c': 300}
    numeros_sara = {'a': 300, 'b': 200, 'd': 400, 'c': 500, 'e': 250}

    atualizar_numeros(numeros_maria, numeros_sara)

    print(f'Os valores do dicionário numeros_maria são: {numeros_maria}')


if __name__ == '__main__':
    main()
