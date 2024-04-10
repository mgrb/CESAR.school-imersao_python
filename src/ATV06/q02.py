"""Questão 02. Substituição de palavras.

Faça um programa que peça ao usuário para inserir:
○ uma frase
○ uma palavra que está contida na frase
○ outra palavra que ele deseja substituir no lugar da primeira palavra inserida.
Por fim, o programa exibe a frase modificada, toda em letra maiúscula.
"""

print('\n\n****\n Questão 02. Substituição de palavras\n****\n')

if __name__ == '__main__':
    frase = input('Informe uma frase: ')
    palavra_original = input('Informe uma palavra contida na frase: ')
    palavra_substituta = input('Informe a palavra substituta: ')

    frase_modificada = frase.replace(palavra_original, palavra_substituta)
    print(frase_modificada.upper())
