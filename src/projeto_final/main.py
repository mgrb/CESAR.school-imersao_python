"""Modulo responsável por iniciar a aplicação AndarDeCimaApp."""

from rich.console import Console
from telas.principal import print_tela_principal
from telas.unidade_habitacional import (
    delegate_control as go_to_unidade_habitacional,
)

csl = Console()
csl.clear()


def main() -> None:
    opc = 0
    while opc != '5':
        opc = print_tela_principal()
        csl.clear()
        match opc:
            case '1':
                go_to_unidade_habitacional()
            case '2':
                print('Moradores')
            case '3':
                print('Áreas Comuns')
            case '4':
                print('Reservas')
            case '5':
                print('Saindo...')
            case _:
                print('Opção inválida')


if __name__ == '__main__':
    main()
    csl.clear()
