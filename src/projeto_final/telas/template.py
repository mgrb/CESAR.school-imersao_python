"""Módulo que contém a estrutura de tela da aplicação."""

from __future__ import annotations

from rich import box, print
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text

PANEL_WIDTH = 100
TITULO_SISTEMA = 'ANDAR DE CIMA - 🏢☝️ :: Gestão Condominial'


def build_title_panel(title: str = TITULO_SISTEMA) -> Panel:
    """Imprime um título na tela."""
    tt = Text(title, justify='center')
    return Panel(
        tt,
        style='blue',
        box=box.DOUBLE_EDGE,
        width=PANEL_WIDTH,
    )


def build_option_panel(title: str, opc: dict[str, str]) -> Panel:
    """Monta um painel de opções."""
    menu_itens = (f'[blue bold]{key}[/]. {value}' for key, value in opc.items())
    return Panel(
        '\n'.join(menu_itens),
        title=title,
        title_align='left',
        box=box.HEAVY_EDGE,
        width=PANEL_WIDTH,
    )


def build_table_panel(title: str, lista: list[dict]) -> Table:
    """Monta um painel de tabela."""
    tabela = Table(title=title, min_width=PANEL_WIDTH, box=box.HORIZONTALS)
    keys = lista[0].keys()

    for key in keys:
        tabela.add_column(key)

    for item in lista:
        valores = [str(item[key]) for key in keys]
        tabela.add_row(*valores)

    return tabela


def build_content_panel(sub_title: str, content: str) -> Panel:
    """Imprime o conteúdo da tela principal."""
    return Panel(
        content,
        title=sub_title,
        title_align='left',
        box=box.HEAVY_EDGE,
        width=PANEL_WIDTH,
    )


def ask_for_option(
    question: str = 'Selecione uma opção',
    opcoes: list = None,
    dft: str = None,
) -> str:
    """Pergunta ao usuário qual opção deseja escolher."""
    return Prompt.ask(f'{question }', choices=opcoes, default=dft)


if __name__ == '__main__':
    pessoas = []
    pessoas.append(
        {'Nome': 'Fulano', 'Idade': 30, 'Sexo': 'M', 'CPF': '123.456.789-00'},
    )
    pessoas.append(
        {'Nome': 'Ciclano', 'Idade': 25, 'Sexo': 'F', 'CPF': '987.654.321-00'},
    )
    pessoas.append(
        {'Nome': 'Beltrano', 'Idade': 40, 'Sexo': 'M', 'CPF': '456.789.123-00'},
    )
    pessoas.append(
        {'Nome': 'Fulana', 'Idade': 35, 'Sexo': 'F', 'CPF': '789.123.456-00'},
    )

    console = Console()
    console.clear()
    with console:
        print(build_title_panel('ANDAR DE CIMA - 🏢☝️ :: Gestão Condominial'))
        print(build_table_panel('Pessoas', pessoas))
        print(
            build_content_panel(
                'Menu Principal',
                '1. Unidades Habitacionais\n2. Moradores\n3. Áreas Comuns\n4. Reservas\n5. Sair',
            ),
        )
        promt_user(['1', '2', '3', '4', '5'])
