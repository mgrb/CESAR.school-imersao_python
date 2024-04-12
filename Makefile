SHEll := /bin/zsh
.PHONY: venv

venv:
	@poetry run poetry install

commit:
	@echo "Revisar mudanças para este commit: "
	@echo "-------------------------------------"
	@git status -s 
	@echo "-------------------------------------"
	@read -p "Mensagem do commit: " msg; \

	@git add .
	@git commit -m "$$(msg)"

update:
	@git fetch origin
	@git pull
	@$(MAKE) venv