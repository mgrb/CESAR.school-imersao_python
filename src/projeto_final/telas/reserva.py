from mem_db import (
    areas_comuns,
    delete_reserva,
    fetch_nested_data_from_reserva,
    find_morador_by_cpf,
    find_reserva_by_id,
    find_reservas_by_data,
    insert_reserva,
    is_area_comum_livre,
    moradores,
    reservas,
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

opc_menu_reserva = {
    '1': 'Listar Reservas',
    '2': 'Reserva de Área Comum',
    '3': 'Cancelar Reserva',
    '4': 'Voltar',
}

opc_busca = {
    '1': 'Buscar por CPF',
    '2': 'Buscar por área comum',
    '3': 'Buscar por data',
    '4': 'Listar todas as reservas',
}


def print_tela_reserva_menu() -> str:
    console = Console()
    with console:
        print(build_title_panel())
        print(
            build_option_panel(
                'Gestão de Reservas',
                opc_menu_reserva,
            ),
        )
        return ask_for_option(opcoes=opc_menu_reserva.keys())


def print_tela_reserva_listar() -> None:
    """Imprime a tela de listagem de Reservas."""
    console = Console()
    with console:
        print(build_title_panel())
        if len(reservas()) == 0:
            print(
                build_content_panel(
                    'Reservas - Listagem',
                    '[blink red b ]Nenhuma reserva cadastrada.[/]',
                ),
            )
        else:
            reservas_nested = fetch_nested_data_from_reserva(reservas())
            print(
                build_table_panel(
                    'Reservas - Listagem',
                    reservas_nested,
                ),
            )
        ask_for_option('Pressione qualquer tecla para continuar...')


def print_tela_reserva_cadastrar() -> None:
    """Imprime a tela de cadastro de Reservas."""
    console = Console()
    with console:
        print(build_title_panel())
        print(
            Text(
                'Nova Reserva de Área Comum',
                style='bold yellow',
                justify='center',
            ),
        )
        print(Text('Informe os dados da reserva:', justify='center'))
        areas = {str(area['id']): area['nome'] for area in areas_comuns()}
        print(build_option_panel('Qual [b]área[/] deseja?', areas))
        area_selecionada = ask_for_option(opcoes=areas.keys())
        data_livre = False
        while not data_livre:
            data_selecioanda = ask_for_option('[b]Data[/] da reserva')
            data_livre = is_area_comum_livre(area_selecionada, data_selecioanda)
            if not data_livre:
                print(Text('Data indisponível, tente outra.', style='red'))

        morador_selecionado = None
        while morador_selecionado is None:
            print(
                build_table_panel(
                    'Selecione o [b]morador[/] responsavel pela reserva',
                    moradores(),
                ),
            )
            morador_selecionado = ask_for_option(
                'Informe o [b]CPF do Morador[/]',
            )
            morador_selecionado = find_morador_by_cpf(morador_selecionado)
            if morador_selecionado is None:
                print(Text('Morador não encontrado.', style='red'))

        insert_reserva(
            int(area_selecionada),
            data_selecioanda,
            morador_selecionado['id'],
        )
        print(
            Text(
                'Reserva cadastrada com sucesso.',
                style='bold green blink',
                justify='center',
            ),
        )
        ask_for_option('Pressione qualquer tecla para continuar...')


def print_tela_reserva_cancelar() -> None:
    console = Console()
    with console:
        print(build_title_panel())
        print(
            Text(
                'Cancelar Reserva de Área Comum',
                style='bold yellow',
                justify='center',
            ),
        )

        print(build_option_panel('Como deseja buscar a reserva?', opc_busca))
        mode_busca_reserva = ask_for_option(opcoes=opc_busca.keys(), dft='4')

        reserva_selecionada = selecionar_reserva(mode_busca_reserva)

        print(build_option_panel('Reserva selecionada', reserva_selecionada))
        confirmacao = ask_for_option(
            'Deseja cancelar a reserva? [b](S)= Sim / (N)=Não[/]',
            dft='N',
        )

        if confirmacao.upper() == 'S':
            delete_reserva(reserva_selecionada['id'])
            print(
                Text(
                    'Reserva cancelada com sucesso!',
                    style='bold green',
                    justify='center',
                ),
            )
    ask_for_option('Pressione qualquer tecla para continuar...')


def selecionar_reserva(modo_busca: str) -> dict:
    """Seleciona uma reserva."""
    reserva = None

    while not reserva:
        reserva_id = None
        match modo_busca:
            case '1':  # Buscar por CPF
                pass
            case '2':  # Buscar por área comum
                pass
            case '3':  # Buscar por data
                data = ask_for_option('Informe uma [b]data[/] (DD/MM/YYYY)')
                reservas = fetch_nested_data_from_reserva(
                    find_reservas_by_data(data),
                )
                print(
                    build_table_panel(
                        f'Reservas para data [b]{data}[/]',
                        reservas,
                    ),
                )
            case '4':  # Listar todas as reservas
                reservas = fetch_nested_data_from_reserva(reservas())
                print(build_table_panel('Reservas - Listagem', reservas))

        reserva_id = ask_for_option('Informe o [b]ID[/] da reserva')
        reserva = find_reserva_by_id(int(reserva_id))
        if reserva is None:
            print(Text('Reserva não encontrada.', style='red'))
            ask_for_option('Pressione qualquer tecla para tentar novamente...')

    return reserva


def delegate_control() -> str:
    console = Console()
    opc = 0

    while opc != '4':
        opc = print_tela_reserva_menu()
        console.clear()
        match opc:
            case '1':
                print_tela_reserva_listar()
            case '2':
                print_tela_reserva_cadastrar()
            case '3':
                print_tela_reserva_cancelar()
            case '4':
                print('Voltando...')
            case _:
                print('Opção inválida')
        console.clear()
    return '0'
