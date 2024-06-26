"""Questão 8. Conversor de temperatura.

Converta uma temperatura em graus Celsius C para Fahrenheit F.
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Converte uma temperatura de Celsius para Fahrenheit.

    INPUT:
        celsius: float - Temperatura em Celsius.
    OUTPUT:
        float - Temperatura em Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


if __name__ == '__main__':
    print(
        '\n\n****\n Conversor de temperatura - Celsius para Fahrenheit \n****\n'
    )
    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f'{celsius:.1f} graus Celsius é {fahrenheit:.1f} graus Fahrenheit.')
