"""Questão 4. Calculadora de Juros Simples.

Peça ao usuário para inserir um valor inicial, a taxa de juro e o tempo.
Calcule e mostre o valor futuro após o período especificado com juros simples.
"""

from communs.util import print_header

if __name__ == '__main__':
    print_header('Calculadora de Juros Simples')
    valor_inicial = float(input('Digite o valor inicial: '))
    taxa_juro = float(input('Digite a taxa de juro: '))
    tempo = int(input('Digite o tempo: '))
    valor_final = valor_inicial * (1 + (taxa_juro / 100) * tempo)
    print(f'Valor final: R$ {valor_final:.2f}')
