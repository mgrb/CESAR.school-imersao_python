"""Modulo responsável por iniciar a aplicação AndarDeCimaApp."""

from telas.principal import show_principal


def main():
    opc = 0
    while opc != '5':
        opc = show_principal()

        match opc:
            case '1':
                print('Unidades Habitacionais')
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
