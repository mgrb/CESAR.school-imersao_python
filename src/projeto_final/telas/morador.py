from mem_db import (
    delete_morador,
    find_morador_by_cpf,
    find_unidade_habitacional_by_id,
    find_unidade_habitacional_by_identificador,
    insert_morador,
    moradores,
    update_morador,
)
from rich import print
from rich.console import Console
from rich.text import Text
from telas.template import (
    ask_for_option,
    build_content_panel,
    build_option_panel,
    build_table_panel,
    build_title_panel,
)

opc_menu_morador = {
    '1': 'Listar Moradores',
    '2': 'Cadastrar Morador',
    '3': 'Alterar Morador',
    '4': 'Excluir Morador',
    '5': 'Voltar',
}


def print_tela_morador_menu() -> None:
    console = Console()
    with console:
        print(build_title_panel())
        print(
            build_option_panel(
                'Cadastro de Moradores',
                opc_menu_morador,
            ),
        )

        return ask_for_option(opcoes=opc_menu_morador.keys())


def print_tela_morador_listar() -> None:
    """Imprime a tela de Moradores."""
    console = Console()
    with console:
        print(build_title_panel())
        if len(moradores()) == 0:
            print(
                build_content_panel(
                    'Moradores - Listagem',
                    '[blink red b ]Nenhum morador cadastrado.[/]',
                ),
            )
        else:
            print(
                build_table_panel(
                    'Moradores - Listagem',
                    moradores(),
                ),
            )

        ask_for_option('Pressione qualquer tecla para continuar...')


def print_tela_morador_cadastrar() -> None:
    """Imprime a tela de cadastro de Moradores."""
    console = Console()
    with console:
        print(build_title_panel())
        print(Text('Novo Morador', style='bold blue', justify='center'))
        print(Text('Informe os seguintes dados do morador', justify='center'))

        nome = ask_for_option('[b]Nome[/]')
        cpf = ask_for_option('[b]CPF[/]')
        email = ask_for_option('[b]Email[/]')
        und_habit = None
        while und_habit is None:
            und_habit_identificador = ask_for_option(
                '[b]Identificador da Unidade Habitacional[/]',
            )
            und_habit = find_unidade_habitacional_by_identificador(
                und_habit_identificador,
            )
            if und_habit is None:
                print(
                    Text(
                        f'Unidade Habitacional [{und_habit_identificador}] não encontrada',
                        style='bold red',
                        justify='center',
                    ),
                )
        insert_morador(cpf, nome, email, und_habit['id'])
        print('Morador cadastrado com sucesso!')
        ask_for_option('Pressione qualquer tecla para continuar...')


def print_tela_morador_alterar() -> None:
    """Imprime a tela de alteração de Moradores."""
    console = Console()
    with console:
        print(build_title_panel())
        print(Text('Alterar Morador', style='bold blue', justify='center'))

        morador = None
        while morador is None:
            morador = find_morador_by_cpf(
                ask_for_option(
                    'Informe o [b]CPF[/] do morador que deseja alterar',
                ),
            )
            if morador is None:
                print(
                    Text(
                        'Morador não encontrado!',
                        style='bold red',
                        justify='center',
                    ),
                )

        print(Text('Informe os novos dados do morador', justify='center'))

        nome = ask_for_option(question='[b]Nome[/]', dft=morador['nome'])
        email = ask_for_option(question='[b]Email[/]', dft=morador['email'])
        unid_habit_atual = find_unidade_habitacional_by_id(
            morador['und_habit_id'],
        )
        und_habit_nova = None
        while und_habit_nova is None:
            und_habit_identificador = ask_for_option(
                question='[b]Identificador da Unidade Habitacional ID[/]',
                dft=unid_habit_atual['identificador'],
            )
            und_habit_nova = find_unidade_habitacional_by_identificador(
                und_habit_identificador,
            )
            if und_habit_nova is None:
                print(
                    Text(
                        f'Unidade Habitacional [{und_habit_identificador}] não encontrada',
                        style='bold red',
                        justify='center',
                    ),
                )

        update_morador(
            morador['id'], morador['cpf'], nome, email, und_habit_nova['id']
        )
        print(
            Text(
                'Morador alterado com sucesso!',
                style='bold green',
                justify='center',
            ),
        )

        ask_for_option('Pressione qualquer tecla para continuar...')


def print_tela_morador_excluir() -> None:
    """Imprime a tela de exclusão de Moradores."""
    console = Console()
    with console:
        print(build_title_panel())
        print(Text('Excluir Morador', style='bold blue', justify='center'))

        morador = None
        while morador is None:
            morador = find_morador_by_cpf(
                ask_for_option(
                    'Informe o [b]CPF[/] do morador que deseja excluir',
                ),
            )
            if morador is None:
                print(
                    Text(
                        'Morador não encontrado!',
                        style='bold red',
                        justify='center',
                    ),
                )

        print(build_option_panel('Morador', morador))

        confirm = ask_for_option(
            question=f'Deseja realmente excluir o morador [b][{morador["nome"]}][/]? [b](S)=Sim / (N)=Não[/]',
            dft='N',
        )
        if confirm.upper() == 'S':
            delete_morador(morador['id'])
            print(
                Text(
                    'Morador excluído com sucesso!',
                    style='bold green',
                    justify='center',
                ),
            )
        else:
            print(
                Text(
                    'Operação cancelada!',
                    style='bold yellow',
                    justify='center',
                ),
            )

        ask_for_option('Pressione qualquer tecla para continuar...')


def delegate_control() -> None:
    """Delega o controle para a tela de Moradores."""
    console = Console()
    opc = '0'
    while opc != '5':
        opc = print_tela_morador_menu()
        console.clear()
        match opc:
            case '1':
                print_tela_morador_listar()
            case '2':
                print_tela_morador_cadastrar()
            case '3':
                print_tela_morador_alterar()
            case '4':
                print_tela_morador_excluir()
            case '5':
                print('Voltando...')
            case _:
                print('Opção inválida')
        console.clear()
