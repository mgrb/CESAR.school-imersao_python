"""Questão 01. Calculadora de Quadrados.

Crie uma função chamada quadrado que recebe um número x como
parâmetro. A função deve retornar um dicionário onde as chaves são os
números de 1 a x e os valores são o quadrado desses números. Teste a função no
programa principal.
"""


class NaoMenorQueUmError(Exception):
    """Exceção para valores menores ou iguais a 1."""

    def __init__(
        self,
        message: str = 'O valor de x deve ser maior que 1.',
    ) -> None:
        """Construtor da classe."""
        super().__init__(message)


def quadrado(x: int) -> dict:
    """Função que retorna o quadrado de todos os números de 1 a x.

    Arguments:
    ---------
        x: {int}  Número maior que 1.

    Returns:
    -------
        dict: Dicionário com os números de 1 a x e seus respectivos quadrados.

    """
    if x <= 1:
        raise NaoMenorQueUmError

    return {i: i**2 for i in range(1, x + 1)}


def main() -> None:
    """Função principal."""
    x = int(input('Digite um número: '))
    print(quadrado(x))


if __name__ == '__main__':
    main()
