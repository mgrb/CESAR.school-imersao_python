SHEll := /bin/zsh
.PHONY: venv

venv:
	@poetry run poetry install

commit:
	@git status -s 
	@git add .
	@git commit -m "$(msg)"

update:
	@git fetch origin
	@git pull
	@$(MAKE) venv