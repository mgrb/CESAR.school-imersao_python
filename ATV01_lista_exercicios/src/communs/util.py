"""Ferramentas úteis para o projeto."""


def print_header(title: str) -> None:
    """Imprime um cabeçalho."""
    size = len(title) + 3
    print(f"\n\n{'*' * size} \n {title} \n{'*' * size}\n")
