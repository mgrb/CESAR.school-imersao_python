"""Questão 10. Sequencia de Fibonacci.

Um matemático deseja explorar variações da famosa sequência de Fibonacci. Em
vez de começar com os números 0 e 1, ele quer começar com dois números
quaisquer e gerar a sequência a partir deles. O usuário deve inserir os dois
primeiros números da sequência.
Em seguida, o programa deve gerar os próximos 20 números da sequência, onde cada
número é a soma dos dois anteriores, assim como na sequência de Fibonacci
tradicional.
Ao final, o programa deve exibir a sequência completa de 22 números.
"""

if __name__ == '__main__':
    print('\n\n****\n Sequencia de Fibonacci \n****\n')

    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    nn = 0

    print('Sequencia:')
    for i in range(20):
        if i == 0:
            print(n1)
            print(n2)

        nn = n1 + n2
        print(nn)

        n1 = n2
        n2 = nn
