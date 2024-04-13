"""Questão 03. Agenda de contatos.

Crie um programa que represente uma agenda de contatos. O programa deve
oferecer as seguintes opções ao usuário:
1. Incluir contato: Permite ao usuário adicionar um nome e um número de
telefone à agenda.
2. Excluir contato: Permite ao usuário remover um contato da agenda
usando o nome como referência.
3. Buscar contato: Permite ao usuário buscar um contato na agenda pelo
nome e exibir o número de telefone correspondente.
4. Finalizar programa.

Crie três funções para realizar cada uma das opções acima: incluir_contato,
excluir_contato e buscar_contato.

● incluir_contato recebe como parâmetro o nome e o telefone
● excluir_contato e buscar_contato recebe como parâmetro o nome

No programa principal, um dicionário deve ser inicializado e o menu com as 4
opções deve ser exibido. Ao selecionar uma delas o usuário deve fornecer os
parâmetros via input e a função equivalente à opção escolhida deve ser chamada.
Ao finalizar o programa todo o dicionário deve ser exibido.
"""

agenda = {}


def incluir_contato(nome: str, telefone: str) -> None:
    """Função que inclui um contato na agenda.

    Arguments:
    ---------
        nome: {str}  Nome do contato.
        telefone: {str}  Telefone do contato.

    """
    agenda[nome] = telefone


def excluir_contato(nome: str) -> bool:
    """Função que exclui um contato da agenda.

    Arguments:
    ---------
        nome: {str}  Nome do contato.

    """
    excluido = agenda.pop(nome, None)
    return excluido is not None


def buscar_contato(nome: str) -> tuple[str, str] | None:
    """Função que busca um contato na agenda.

    Arguments:
    ---------
        nome: {str}  Nome do contato.

    Returns:
    -------
        str: Telefone do contato.

    """
    contato = agenda.get(nome)

    return (nome, contato) if contato is not None else None


def main() -> None:
    """Função principal."""
    print('Agenda de Contatos')
    while True:
        print('1. Incluir contato')
        print('2. Excluir contato')
        print('3. Buscar contato')
        print('4. Finalizar programa')

        opcao = input('Digite a opção desejada: ')

        match opcao:
            case '1':
                nome = input('Digite o nome do contato: ')
                telefone = input('Digite o telefone do contato: ')
                incluir_contato(nome, telefone)
                print('Contato adicionado com sucesso!')
            case '2':
                nome = input('Digite o nome do contato: ')
                is_excluido = excluir_contato(nome)
                print(
                    'Contato excluído com sucesso!'
                    if is_excluido
                    else 'Contato não encontrado na agenda.',
                )
            case '3':
                nome = input('Digite o nome do contato: ')
                contato = buscar_contato(nome)
                if contato is not None:
                    print(f'Número de telefone de {contato[0]}: {contato[1]}')
                else:
                    print('Contato não encontrado na agenda.')

            case '4':
                break
            case _:
                print('Opção inválida!')
    print(agenda)


if __name__ == '__main__':
    main()
