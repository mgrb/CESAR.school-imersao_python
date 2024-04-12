"""Questão 07 Agenda de Contatos.

Crie um programa que represente uma agenda de contatos. O programa deve
oferecer as seguintes opções ao usuário:

    1. Incluir contato: Permite ao usuário adicionar um nome e um número de
    telefone à agenda.
    2. Excluir contato: Permite ao usuário remover um contato da agenda
    usando o nome como referência.
    3. Buscar contato: Permite ao usuário buscar um contato na agenda pelo
    nome e exibir o número de telefone correspondente.
    4. Sair. Exibe todo o dicionário e a mensagem “Programa finalizado.”.

Use um dicionário onde as chaves são os nomes dos contatos e os valores são os
números de telefone.
"""

if __name__ == '__main__':
    print('\n\n****\n Questão 07. Agenda de Contatos\n****\n')

    agenda = {}

    while True:
        print('\n --------------------------\n Opções:')
        print('1. Incluir contato')
        print('2. Excluir contato')
        print('3. Buscar contato')
        print('4. Sair \n --------------------------\n')

        opcao = input('Escolha uma opção: ')

        match opcao:
            case '1':
                nome = input('Informe o nome do contato: ')
                telefone = input('Informe o telefone do contato: ')
                agenda[nome] = telefone
                print('Contato adicionado com sucesso!')

            case '2':
                nome = input('Informe o nome do contato: ')
                removido = agenda.pop(nome, None)
                print('Contato não encontrado.') if removido is None else print(
                    'Contato excluído com sucesso!',
                )
            case '3':
                nome = input('Informe o nome do contato: ')
                tel_num = agenda.get(nome)
                print(
                    'Contato não encontrado na agenda.',
                ) if tel_num is None else print(
                    f'Número de telefone de {nome}: {tel_num}',
                )
            case '4':
                print(agenda)
                print('Programa finalizado.')
                break
            case _:
                print('Opção inválida.')
