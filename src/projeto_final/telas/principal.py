"""Telas da aplicação.

Suite de funç~oes que montam as telas da aplicação.
"""

from __future__ import annotations

from rich import print
from rich.console import Console
from telas.template import (
    ask_for_option,
    build_option_panel,
    build_title_panel,
)

opc_menu_principal = {
    '1': 'Unidades Habitacionais',
    '2': 'Moradores',
    '3': 'Áreas Comuns',
    '4': 'Reservas',
    '5': 'Sair',
}


def print_tela_principal() -> str:
    """Imprime a tela principal do sistema."""
    console = Console()
    with console:
        print(build_title_panel())
        print(build_option_panel('Menu Principal', opc_menu_principal))
        return ask_for_option(opcoes=opc_menu_principal.keys())
