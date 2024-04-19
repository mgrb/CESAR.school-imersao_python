"""Módulo que contém a estrutura de memória da aplicação."""

MORADORES_DB = []
AREAS_COMUNS_DB = []
RESERVAS_DB = []
UNIDADES_HABITACIONAIS_DB = []

morador_last_id = 0
area_comum_last_id = 0
reserva_last_id = 0
unidade_habitacional_last_id = 0


def insert_morador(cpf: str, nome: str, email: str, und_habit_id: int) -> None:
    """Insere um morador no banco de dados."""
    global morador_last_id
    morador_last_id += 1
    MORADORES_DB.append(
        {
            'id': morador_last_id,
            'cpf': cpf,
            'nome': nome,
            'email': email,
            'und_habit_id': und_habit_id,
        },
    )


def update_morador(
    id: int,
    cpf: str,
    nome: str,
    email: str,
    und_habit_id: int,
) -> None:
    """Atualiza um morador no banco de dados."""
    for morador in MORADORES_DB:
        if morador['id'] == id:
            morador['cpf'] = cpf
            morador['nome'] = nome
            morador['email'] = email
            morador['und_habit_id'] = und_habit_id
            break


def delete_morador(id: int) -> None:
    """Remove um morador do banco de dados."""
    for morador in MORADORES_DB:
        if morador['id'] == id:
            MORADORES_DB.remove(morador)
            break


def find_morador_by_cpf(cpf: str) -> dict:
    """Busca um morador pelo CPF."""
    for morador in MORADORES_DB:
        if morador['cpf'] == cpf:
            return morador
    return None


def moradores() -> list[dict]:
    """Retorna todos os moradores cadastrados."""
    return MORADORES_DB


def insert_unidade_habitacional(
    identificador: str,
    proprietario: str,
    email: str,
    caracteristicas: str,
) -> None:
    """Insere uma unidade habitacional no banco de dados."""
    global unidade_habitacional_last_id
    unidade_habitacional_last_id += 1
    UNIDADES_HABITACIONAIS_DB.append(
        {
            'id': unidade_habitacional_last_id,
            'identificador': identificador,
            'proprietario': proprietario,
            'email': email,
            'caracteristicas': caracteristicas,
        },
    )


def update_unidade_habitacional(
    id: int,
    identificador: str,
    proprietario: str,
    email: str,
    caracteristicas: str,
) -> None:
    """Atualiza uma unidade habitacional no banco de dados."""
    for unidade_habitacional in UNIDADES_HABITACIONAIS_DB:
        if unidade_habitacional['id'] == id:
            unidade_habitacional['identificador'] = identificador
            unidade_habitacional['proprietario'] = proprietario
            unidade_habitacional['email'] = email
            unidade_habitacional['caracteristicas'] = caracteristicas
            break


def delete_unidade_habitacional(id: int) -> None:
    """Remove uma unidade habitacional do banco de dados."""
    for unidade_habitacional in UNIDADES_HABITACIONAIS_DB:
        if unidade_habitacional['id'] == id:
            UNIDADES_HABITACIONAIS_DB.remove(unidade_habitacional)
            break


def find_unidade_habitacional_by_identificador(identificador: str) -> dict:
    """Busca uma unidade habitacional pelo identificador."""
    for unidade_habitacional in UNIDADES_HABITACIONAIS_DB:
        if unidade_habitacional['identificador'] == identificador:
            return unidade_habitacional
    return None


def find_unidade_habitacional_by_id(id: int) -> dict:
    """Busca uma unidade habitacional pelo id."""
    for unidade_habitacional in UNIDADES_HABITACIONAIS_DB:
        if unidade_habitacional['id'] == id:
            return unidade_habitacional
    return None


def unidades_habitacionais() -> list[dict]:
    """Retorna todas as unidades habitacionais cadastradas."""
    return UNIDADES_HABITACIONAIS_DB


def insert_area_comum(nome: str, descricao: str) -> None:
    """Insere uma área comum no banco de dados."""
    global area_comum_last_id
    area_comum_last_id += 1
    AREAS_COMUNS_DB.append(
        {
            'id': area_comum_last_id,
            'nome': nome,
            'descricao': descricao,
        },
    )


def update_area_comum(id: int, nome: str, descricao: str) -> None:
    """Atualiza uma área comum no banco de dados."""
    for area_comum in AREAS_COMUNS_DB:
        if area_comum['id'] == id:
            area_comum['nome'] = nome
            area_comum['descricao'] = descricao
            break


def delete_area_comum(id: int) -> None:
    """Remove uma área comum do banco de dados."""
    for area_comum in AREAS_COMUNS_DB:
        if area_comum['id'] == id:
            AREAS_COMUNS_DB.remove(area_comum)
            break


def find_area_comum_by_nome(nome: str) -> dict:
    """Busca uma área comum pelo nome."""
    for area_comum in AREAS_COMUNS_DB:
        if area_comum['nome'] == nome:
            return area_comum
    return None


def find_area_comum_by_id(id: int) -> dict:
    """Busca uma área comum pelo id."""
    for area_comum in AREAS_COMUNS_DB:
        if area_comum['id'] == id:
            return area_comum
    return None


def areas_comuns() -> list[dict]:
    """Retorna todas as áreas comuns cadastradas."""
    return AREAS_COMUNS_DB


def reservas() -> list[dict]:
    """Retorna todas as reservas cadastradas."""
    return RESERVAS_DB


# INIT SEEDED DATA
insert_unidade_habitacional('101', 'Fulano', 'fulano@uol.com', '3 quartos')
insert_unidade_habitacional('102', 'Ciclano', 'ciclano@aol.com', '2 quartos')
insert_unidade_habitacional('103', 'Beltrano', 'beltrano@bol.com', '1 quarto')
insert_unidade_habitacional('104', 'Fátima', 'fafa@ig.com.br', '4 quartos')

insert_morador('123.456.789-00', 'Fulano', 'fulano@uol.com', 1)
insert_morador('987.654.321-00', 'Ciclano', 'ciclano@aol.com', 2)
insert_morador('456.789.123-00', 'Geronimo', 'gege@terra.com.br', 3)
