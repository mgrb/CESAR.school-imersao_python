"""Modulo responsável por iniciar a aplicação AndarDeCimaApp."""

from rich.console import Console
from telas.area_comum import delegate_control as go_to_area_comum
from telas.morador import delegate_control as go_to_morador
from telas.principal import print_tela_principal
from telas.reserva import delegate_control as go_to_reserva
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
                go_to_morador()
            case '3':
                go_to_area_comum()
            case '4':
                go_to_reserva()
            case '5':
                print('Saindo...')
            case _:
                print('Opção inválida')


if __name__ == '__main__':
    main()
    csl.clear()
