from mem_db import (
    areas_comuns,
    delete_area_comum,
    find_area_comum_by_id,
    insert_area_comum,
    update_area_comum,
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

opc_menu_area_comum = {
    '1': 'Listar Áreas Comuns',
    '2': 'Cadastrar Área Comum',
    '3': 'Alterar Área Comum',
    '4': 'Excluir Área Comum',
    '5': 'Voltar',
}


def print_tela_area_comum_menu() -> str:
    console = Console()
    with console:
        print(build_title_panel())
        print(
            build_option_panel(
                'Cadastro de Áreas Comuns',
                opc_menu_area_comum,
            ),
        )
        return ask_for_option(opcoes=opc_menu_area_comum.keys())


def print_tela_area_comum_listar() -> None:
    console = Console()
    with console:
        print(build_title_panel())
        if len(areas_comuns()) == 0:
            print(
                build_content_panel(
                    'Áreas Comuns - Listagem',
                    '[blink red b ]Nenhuma área comum cadastrada.[/]',
                ),
            )
        else:
            print(
                build_table_panel(
                    'Áreas Comuns - Listagem',
                    areas_comuns(),
                ),
            )
    ask_for_option('Pressione qualquer tecla para continuar...')


def print_tela_area_comum_cadastrar() -> None:
    console = Console()
    with console:
        print(build_title_panel())
        print(
            Text(
                'Nova Área Comum',
                style='bold underline',
            ),
        )

        print(
            Text(
                'Informe os seguintes dados da  área comum.',
                justify='center',
            ),
        )

        nome = ask_for_option('[b]Nome[/]')
        descricao = ask_for_option('[b]Descrição[/]')

        insert_area_comum(nome, descricao)
        print(
            Text(
                'Área comum cadastrada com sucesso!',
                style='bold green',
                justify='center',
            ),
        )
        ask_for_option('Pressione qualquer tecla para continuar...')


def print_tela_area_comum_alterar() -> None:
    """Imprime a tela de alteração de Áreas Comuns."""
    console = Console()
    with console:
        print(build_title_panel())
        print(
            Text(
                'Alterar Área Comum',
                style='bold yellow',
            ),
        )

        area_comum = None
        while area_comum is None:
            area_comum_id = int(
                ask_for_option(
                    'Informe o [b]ID[/] da área comum a ser alterada',
                ),
            )
            area_comum = find_area_comum_by_id(area_comum_id)

            if area_comum is None:
                print(
                    Text(
                        'Área comum não encontrada.',
                        style='bold red',
                        justify='center',
                    ),
                )

        print(
            Text(
                'Informe os novos dados da área comum.',
                justify='center',
            ),
        )

        nome = ask_for_option('[b]Nome[/]', dft=area_comum['nome'])
        descricao = ask_for_option(
            '[b]Descrição[/]',
            dft=area_comum['descricao'],
        )

        update_area_comum(area_comum['id'], nome, descricao)
        print(
            Text(
                'Área comum alterada com sucesso!',
                style='bold green',
                justify='center',
            ),
        )
        ask_for_option('Pressione qualquer tecla para continuar...')


def print_tela_area_comum_excluir() -> None:
    """Imprime a tela de exclusão de Áreas Comuns."""
    console = Console()
    with console:
        print(build_title_panel())
        print(
            Text(
                'Excluir Área Comum',
                style='bold yellow',
                justify='center',
            ),
        )

        area_comum = None
        while area_comum is None:
            area_comum_id = int(
                ask_for_option(
                    'Informe o [b]ID[/] da área comum a ser excluída',
                )
            )
            area_comum = find_area_comum_by_id(area_comum_id)

            if area_comum is None:
                print(
                    Text(
                        'Área comum não encontrada.',
                        style='bold red',
                        justify='center',
                    ),
                )

        print(build_option_panel('Dados da Área Comum', area_comum))

        confirmacao = ask_for_option(
            f'Deseja realmente excluir a área comum [b]{area_comum['nome']}[/]? (s/n)',
            dft='N',
        )

        if confirmacao.upper() == 'S':
            delete_area_comum(area_comum['id'])
            print(
                Text(
                    'Área comum excluída com sucesso!',
                    style='bold green',
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

        ask_for_option('Pressione qualquer tecla para continuar...')


def delegate_control() -> str:
    console = Console()
    opc = 0

    while opc != '5':
        opc = print_tela_area_comum_menu()
        console.clear()
        match opc:
            case '1':
                print_tela_area_comum_listar()
            case '2':
                print_tela_area_comum_cadastrar()
            case '3':
                print_tela_area_comum_alterar()
            case '4':
                print_tela_area_comum_excluir()
            case '5':
                return '5'
            case _:
                print('Opção inválida. Tente novamente.')
        console.clear()
    return '0'
