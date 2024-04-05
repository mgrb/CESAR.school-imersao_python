SHEll := /bin/zsh
.PHONY: venv install_requirements

venv:
	@poetry shell -n

install_requirements:
	@poetry install