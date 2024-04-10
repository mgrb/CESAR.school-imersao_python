"""Questão 04. Senha do Google Classroom.

Por conta da pandemia, o CEF (Curso Estudante Feliz) adotou o Google Classroom
como ferramenta para auxiliar o ensino remoto. Para acessá-lo, os estudantes
precisam logar com e-mail institucional e senha. A senha inicial, enviada pela
Agenda Digital, é gerada automaticamente a partir da data de nascimento do
aluno, do seguinte modo:

○ mm + ‘$’ + dd(invertido) + ‘#’ + dd + ‘!’ + mm(invertido) + ‘*’ + aaaa

Escreva um programa que leia o dia, mês e ano de nascimento de um estudante e
informe a senha de acordo com a formatação acima.
"""

print('\n\n****\n Questão 04. Senha do Google Classroom\n****\n')

if __name__ == '__main__':
    dia = input('Informe o dia de nascimento: ')
    mes = input('Informe o mês de nascimento: ')
    ano = input('Informe o ano de nascimento: ')

    senha = f'{mes}${dia[::-1]}#{dia}!{mes[::-1]}*{ano}'
    print(f'Sua senha é: {senha}')
