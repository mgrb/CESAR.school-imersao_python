from mem_db import (
    delete_unidade_habitacional,
    find_unidade_habitacional_by_identificador,
    insert_unidade_habitacional,
    unidades_habitacionais,
    update_unidade_habitacional,
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

opc_menu_unidade_habitacional = {
    '1': 'Listar Unidades Habitacionais',
    '2': 'Cadastrar Unidade Habitacional',
    '3': 'Alterar Unidade Habitacional',
    '4': 'Excluir Unidade Habitacional',
    '5': 'Voltar',
}


def print_tela_unidade_habitacional_menu() -> str:
    """Imprime a tela de Unidades Habitacionais."""
    console = Console()
    with console:
        print(build_title_panel())
        print(
            build_option_panel(
                'Cadastro de Unidades Habitacionais',
                opc_menu_unidade_habitacional,
            ),
        )
        return ask_for_option(opcoes=opc_menu_unidade_habitacional.keys())


def print_tela_unidade_habitacional_listar() -> None:
    """Imprime a tela de Unidades Habitacionais."""
    console = Console()
    with console:
        print(build_title_panel())
        if len(unidades_habitacionais()) == 0:
            print(
                build_content_panel(
                    'Unidades Habitacionais - Listagem',
                    '[blink red b ]Nenhuma unidade habitacional cadastrada.[/]',
                ),
            )
        else:
            print(
                build_table_panel(
                    'Unidades Habitacionais - Listagem',
                    unidades_habitacionais(),
                ),
            )

        ask_for_option('Pressione qualquer tecla para voltar...')


def print_tela_unidade_habitacional_cadastrar() -> None:
    """Imprime a tela de cadastro de Unidades Habitacionais."""
    console = Console()
    with console:
        print(build_title_panel())
        print(
            Text(
                'Nova Unidade Habitacional',
                style='bold yellow',
                justify='center',
            ),
        )
        print(
            Text(
                'Informe os seguintes dados da unidade',
                justify='center',
            ),
        )

        identificador = ask_for_option('[b]Identificador[/]')
        proprietario = ask_for_option('[b]Nome do propriétário[/]')
        email = ask_for_option('[b]E-mail do propriétário[/]')
        caracteriasticas = ask_for_option('[b]Características da unidade[/]')

        insert_unidade_habitacional(
            identificador,
            proprietario,
            email,
            caracteriasticas,
        )
        print(
            Text(
                'Unidade Habitacional cadastrada com sucesso!',
                style='bold green blink',
                justify='center',
            ),
        )
        ask_for_option(
            'Pressione qualquer tecla para voltar...',
        )


def print_tela_unidade_habitacional_alterar() -> None:
    """Imprime a tela de alteração de Unidades Habitacionais."""
    console = Console()
    with console:
        print(build_title_panel())
        print(
            Text(
                'Alterar Unidade Habitacional',
                style='bold yellow',
                justify='center',
            ),
        )

        und_habit = None
        while not und_habit:
            identificador = ask_for_option(
                'Informe o [b]Identificador[/] da unidade a ser alterada',
            )
            und_habit = find_unidade_habitacional_by_identificador(
                identificador,
            )
            if und_habit is None:
                print(
                    Text(
                        'Unidade Habitacional não encontrada!',
                        style='bold red',
                        justify='center',
                    ),
                )

        print(
            Text(
                'Informe os novos dados da unidade',
                justify='center',
            ),
        )
        proprietario = ask_for_option(
            question='[b]Nome do propriétário[/]',
            dft=und_habit['proprietario'],
        )
        email = ask_for_option(
            question='[b]E-mail do propriétário[/]',
            dft=und_habit['email'],
        )
        caracteristicas = ask_for_option(
            question='[b]Características da unidade[/]',
            dft=und_habit['caracteristicas'],
        )

        update_unidade_habitacional(
            und_habit['id'],
            und_habit['identificador'],
            proprietario,
            email,
            caracteristicas,
        )
        print(
            Text(
                'Unidade Habitacional alterada com sucesso!',
                style='bold green blink',
                justify='center',
            ),
        )

        ask_for_option(
            'Pressione qualquer tecla para voltar...',
        )


def print_tela_unidade_habitacional_excluir() -> None:
    """Imprime a tela de exclusão de Unidades Habitacionais."""
    console = Console()
    with console:
        print(build_title_panel())
        print(
            Text(
                'Excluir Unidade Habitacional',
                style='bold yellow',
                justify='center',
            ),
        )

        und_habit = None
        while not und_habit:
            identificador = ask_for_option(
                'Informe o [b]Identificador[/] da unidade a ser excluída',
            )
            und_habit = find_unidade_habitacional_by_identificador(
                identificador,
            )
            if und_habit is None:
                print(
                    Text(
                        'Unidade Habitacional não encontrada!',
                        style='bold red',
                        justify='center',
                    ),
                )

        print(
            build_option_panel('Dados da Unidade Habitacional', und_habit),
        )

        confirm = ask_for_option(
            question=f'Deseja realmente excluir a unidade habitacional [b]{und_habit["identificador"]}[/]? [b](S)= Sim / (N)=Não[/]',
            dft='N',
        )
        if confirm.upper() == 'S':
            delete_unidade_habitacional(und_habit['id'])
            print(
                Text(
                    'Unidade Habitacional excluída com sucesso!',
                    style='bold green blink',
                    justify='center',
                ),
            )
        else:
            print(
                Text(
                    'Exclusão cancelada!',
                    style='bold red',
                    justify='center',
                ),
            )

        ask_for_option(
            'Pressione qualquer tecla para voltar...',
        )


def delegate_control() -> str:
    """Delega o controle para a tela de Unidades Habitacionais."""
    console = Console()
    opc = 0
    while opc != '5':
        opc = print_tela_unidade_habitacional_menu()
        console.clear()
        match opc:
            case '1':  # LISTAR
                print_tela_unidade_habitacional_listar()
            case '2':  # CADASTRAR
                print_tela_unidade_habitacional_cadastrar()
            case '3':  # ALTERAR
                print_tela_unidade_habitacional_alterar()
            case '4':  # EXCLUIR
                print_tela_unidade_habitacional_excluir()
            case '5':  # VOLTAR
                print('Voltando...')
            case _:
                print('Opção inválida')
        console.clear()
    return '0'
