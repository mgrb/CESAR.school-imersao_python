# CESAR.school - Imersão Python 🐍
![image](/docs/header.jpg)
Repositório destinado as implementações de soluções para as listas de exercicios da disciplina de Imersão em Python.

> **CESAR.School** \
Imersão Python \
Professora: Joyce Teixeira

## Organização
1. **ATV 01** - Conceitos Básicos, Constantes e Variáveis, Entradas e Saídas: [PDF](docs/exe_list_01-20240402.pdf) - [Code](src/ATV01/)
1. **ATV 02** - Operadores [Link](https://forms.gle/BD66WMhx7QpwPcN36?authuser=0) 
1. **ATV 03** - Instruções de Decisão: [PDF](docs/exe_list_03-20240403.pdf) - [Code](src/ATV03/)

Cada questão da lista foi resolvida em um script a parte dentro do diretório de sua respectiva lista de exercícios.
- Questão 01 -> q01.py
- Questão 02 -> q02.py
- Questão 03 -> q03.py
- ...

### Estrutura de diretórios
```
/
├─📁 .devcontainer   ->  [Configurações do devcontainer]
├─📁 docs            ->  [Listas em PDF]
├─📁 .git            ->  [Configurações do git]
├─📁 src             ->  [Código das soluções divididos
│   ├─📁 ATV01            por listas/questão]
│   │   ├─🐍 q01.py
│   │   ├─🐍 q02.py
│   │   ├─🐍 q03.py
│   │   ...
│   ├─📁 ATV03
│   │   ...
│   └─📁 communs     ->  [Funções comuns utilizadas nas soluções]
├─📁 .vscode         ->  [Definições de ambiente para o VSCode]
├─📄 .gitignore
├─📄 Makefile        ->  [Automações para o ambiente]
├─📄 pyproject.toml  ->  [Definições para o projeto]
├─📄 README.md
└─📄 ruff.toml       ->  [Regras de linter e formarter]
```


## Instanciar e contribuir

Para mais detalhes de como instanciar o ambiente deste projeto e contribuir, ver [aqui](/CONTRIBUTING.md).

