from mem_db import insert_unidade_habitacional, unidades_habitacionais
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


def print_tela_unidade_habitacional_listar() -> str:
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
        return '0'


def print_tela_unidade_habitacional_cadastrar() -> str:
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
        return '0'


def delegate_control() -> str:
    """Delega o controle para a tela de Unidades Habitacionais."""
    console = Console()
    opc = 0
    while opc != '5':
        opc = print_tela_unidade_habitacional_menu()
        console.clear()
        match opc:
            case '1':
                opc = print_tela_unidade_habitacional_listar()
            case '2':
                opc = print_tela_unidade_habitacional_cadastrar()
            case '3':
                print('Alterar Unidade Habitacional')
            case '4':
                print('Excluir Unidade Habitacional')
            case '5':
                print('Voltando...')
            case _:
                print('Opção inválida')
        console.clear()
    return '0'
