# [🏢☝️] Andar de Cima

Sistema para gestão de condomínios habitacionais.

**Andar de Cima** é uma solução abrangente e eficiente projetada para simplificar e otimizar todas as operações relacionadas à administração de condomínios habitacionais. Com uma interface intuitiva e recursos robustos, oferecemos uma plataforma centralizada para gerenciar todas as atividades, como o cadastro de moradores e gestão das áreas comuns, proporcionando transparência, eficiência e segurança.

## Funcionalidades

1. [Cadastro de **Unidades Habitacionais**](#cadastro-de-unidades-habitacionais):
    - Inclui unidade habitacional;
    - Altera unidade habitacional;
    - Exclui unidade habitacional; e
    - Listar unidades habitacionais.
1. Cadastro de **Moradores**:
    - Inclui morador;
    - Altera morador;
    - Exclui morador; e
    - Listar moradores.
1. Cadastro de **Áreas Comuns**:
    - Inclui área comum;
    - Altera área comun;
    - Exclui área comun; e
    - Listar área comuns.
1. Gestão de **Reservas de Áreas Comuns**:
    - Agendamento de área comum;
    - Reagendamento de área comum;
    - Cancelamento de agendamento; e
    - Listar agendamentos.

## Definições

As caracteristicas que são gerenciadas pelo sistema são as seguintes:

### Unidade Habitacional

    - ID: Número que identifica a unidade habtacional.
    - PROPRIETÁRIO: Nome do proprietário.
    - CONTATO: email do proprietário.
    - CARACTERISTICAS: Descrição da unidade habitacional.

### Morador Responsável

    - CPF: Documento identificador do morador.
        > Somento numeros com 11 posições.
    - NOME: Nome do morador.
    - CONTATO: email do morador.
        > Deve atender a definição de um email válido.
    - QTD CO-HABITANTES: Quantidade de pessoasl que moram com o responsável.
    - UNIDADE: ID da unidade habitacional.

### Área Comum

    - CODIGO: Identificador da área.
    - NOME: Nome da área.
    - DESCRIÇÃO: Caracteristicas da área.

### Agendamento

    - MORADOR RESPONSAVEL: CPF do morador responsável.
        > Deve apontar para um CPF já cadastrado em [Morador Responsável](#morador-responsável)
    - CODIGO ÁREA: Identificador da área.
        > Deve apontar para um código já cadastrado em [Área Comum](#área-comum)
    - DATA: Data da reserva.
        > Deve usar o formato "DD/MM/YYY"

## Especificações Funcionais (Stories)

### Cadastro de Unidades Habitacionais

Como  usuário do sistema desejo manter o cadastro das unidades habitacionais, para que possa manter um resgistro da estrutura do condomino que administro.

#### CENARIO 1 - Inclusão de unidade

    - [DADO] que o usuário acesse o meno de inserir unidade;
    - [QUANDO] ele entrar com os dados referente a unidade que deseja incluir, seguindo as definições descritas em [Unidade Habitacional](#unidade-habitacional) corretamente;
    - [ENTÃO] o sistema guardará estas informações e informará ao usuário que o cadastro ocorreu com sucesso.