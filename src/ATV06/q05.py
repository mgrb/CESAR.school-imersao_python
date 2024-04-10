"""Questão 05. Correção de número de celular.

Faça um programa que leia um número de celular, e corrija o número no caso deste
conter somente 8 dígitos, adicionando o '9' na frente. O usuário pode informar
o número com ou sem o traço separador.
"""

print('\n\n****\n Questão 05. Correção de número de celular\n****\n')

if __name__ == '__main__':
    numero = input('Informe o número de celular: ')
    legal_size = 10 if '-' in numero else 9

    if len(numero) < legal_size:
        numero = f'9{numero}'
    print(f'O número corrigido é: {numero}')
