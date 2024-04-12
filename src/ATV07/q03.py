"""Questão 03. Plantão de Técnicos em Enfermagem.

 No Hospital Todos Juntos, a escala de plantão dos técnicos em enfermagem,
para o mês de novembro, está sendo definida. Há 30 técnicos. Faça um
programa que armazene o nome e o dia de trabalho (1 a 30) de cada técnico.
Caso o usuário digite um dia inválido, deverá permanecer no loop até digitar um
dia entre 1 e 30. Por fim, separe em duas tuplas que terão os nomes e os dias de
trabalhos dos funcionários. Uma tupla constará os funcionários que irão
trabalhar em dia par e a outra os funcionários que irão trabalhar em dia ímpar.
Atenção: o primeiro index de cada tupla será o nome e o segundo index será o
dia de trabalho. As duas tuplas juntas devem conter informações sobre os 30
técnicos.
"""

if __name__ == '__main__':
    print('\n\n****\n Questão 03. Plantão de Técnicos em Enfermagem\n****\n')

    tecnicos = []
    dias = []

    QTD_TECNICOS = 30
    MES_LIMITES = (1, 30)

    for i in range(QTD_TECNICOS):
        nome = input(f'Informe o nome do técnico {i+1}: ')
        dia = 0
        while dia < MES_LIMITES[0] or dia > MES_LIMITES[1]:
            dia = int(
                input(
                    f'Informe o dia de trabalho do técnico {i+1} ({MES_LIMITES[0]} a {MES_LIMITES[1]}): ',
                ),
            )
            if dia < MES_LIMITES[0] or dia > MES_LIMITES[1]:
                print(
                    f'Dia inválido! Digite um dia entre {MES_LIMITES[0]} e {MES_LIMITES[1]}',
                )

        tecnicos.append(nome)
        dias.append(dia)

    tecnicos_par = ([], [])
    tecnicos_impar = ([], [])

    for i in range(len(dias)):
        if dias[i] % 2 == 0:
            tecnicos_par[0].append(tecnicos[i])
            tecnicos_par[1].append(dias[i])
        else:
            tecnicos_impar[0].append(tecnicos[i])
            tecnicos_impar[1].append(dias[i])

    print(f'\nTécnicos que trabalharão em dias pares: {tecnicos_par}')
    print(f'Técnicos que trabalharão em dias ímpares: {tecnicos_impar}\n')
