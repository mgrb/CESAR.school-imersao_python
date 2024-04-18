"""Telas da aplicação.

Suite de funç~oes que montam as telas da aplicação.
"""

from rich import box, print
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

opc_menu_principal = {
    '1': 'Unidades Habitacionais',
    '2': 'Moradores',
    '3': 'Áreas Comuns',
    '4': 'Reservas',
    '5': 'Sair',
}


def build_title_panel(title: str) -> Panel:
    """Imprime um título na tela."""
    tt = Text(title)
    return Panel(
        tt,
        style='blue',
        box=box.DOUBLE_EDGE,
    )


def build_content_panel() -> Panel:
    """Imprime o conteúdo da tela principal."""
    menu_itens = (
        f'[blue bold]{key}[/]. {value}'
        for key, value in opc_menu_principal.items()
    )

    return Panel(
        '\n'.join(menu_itens),
        title='Menu Principal',
        title_align='left',
        box=box.HEAVY_EDGE,
    )


def ask_for_option(options: list) -> str:
    """Pergunta ao usuário qual opção deseja escolher."""
    return Prompt.ask('Escolha uma opção: ', choices=options)


def show_principal() -> str:
    """Monta a tela principal da aplicação."""
    console = Console()
    console.clear()

    titulo = 'ANDAR DE CIMA - 🏢☝️'

    with console:
        print(build_title_panel(titulo))
        print(build_content_panel())
        return ask_for_option(opc_menu_principal.keys())
