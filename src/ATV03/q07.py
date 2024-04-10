"""Questão 07: Calculadora de Fatura.

Uma operadora de telefonia móvel deseja oferecer planos personalizados para seus
clientes. Eles oferecem três tipos de planos com diferentes franquias de minutos
e internet:

● Plano Básico: 100 minutos e 5GB de internet por R$ 50.
● Plano Intermediário: 300 minutos e 10GB de internet por R$ 80.
● Plano Avançado: 500 minutos e 20GB de internet por R$ 120.

Caso o cliente ultrapasse a franquia de minutos, será cobrado R$ 1 por minuto
adicional. Se ultrapassar a franquia de internet, será cobrado R$ 10 por GB
adicional. Escreva um programa que peça ao usuário para escolher um plano,
informar quantos minutos e quantos GB ele utilizou no mês. O programa deve
calcular e mostrar o valor total da fatura.
"""

VALOR_FRANQUIA_BASICO: int = 50
VALOR_FRANQUIA_INTERMEDIARIO: int = 80
VALOR_FRANQUIA_AVANCADO: int = 120

COTA_MINUTOS_BASICO: int = 100
COTA_MINUTOS_INTERMEDIARIO: int = 300
COTA_MINUTOS_AVANCADO: int = 500

COTA_GB_BASICO: int = 5
COTA_GB_INTERMEDIARIO: int = 10
COTA_GB_AVANCADO: int = 20

TAXA_MINUTO_ADICIONAL: int = 1
TAXA_GB_ADICIONAL: int = 10

if __name__ == '__main__':
    print('\n\n****\n Calculadora de Fatura \n****\n')

    plano: int = int(
        input('Escolha o plano (1-Básico, 2-Intermediário, 3-Avançado): '),
    )

    minutos: int = int(input('Digite a quantidade de minutos utilizados: '))
    gb: int = int(input('Digite a quantidade de GB utilizados: '))

    valor_total: float = 0

    match plano:
        case 1:
            valor_total = VALOR_FRANQUIA_BASICO
            if minutos > COTA_MINUTOS_BASICO:
                valor_total += (
                    minutos - COTA_MINUTOS_BASICO
                ) * TAXA_MINUTO_ADICIONAL
            if gb > COTA_GB_BASICO:
                valor_total += (gb - COTA_GB_BASICO) * TAXA_GB_ADICIONAL
        case 2:
            valor_total = VALOR_FRANQUIA_INTERMEDIARIO
            if minutos > COTA_MINUTOS_INTERMEDIARIO:
                valor_total += minutos - COTA_MINUTOS_INTERMEDIARIO
            if gb > COTA_GB_INTERMEDIARIO:
                valor_total += (gb - COTA_GB_INTERMEDIARIO) * TAXA_GB_ADICIONAL
        case 3:
            valor_total = VALOR_FRANQUIA_AVANCADO
            if minutos > COTA_MINUTOS_AVANCADO:
                valor_total += minutos - COTA_MINUTOS_AVANCADO
            if gb > COTA_GB_AVANCADO:
                valor_total += (gb - COTA_GB_AVANCADO) * TAXA_GB_ADICIONAL
        case _:
            print('Plano inválido.')

    print(f'Valor da fatura: R$ {valor_total:.2f}')
