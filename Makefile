SHEll := /bin/zsh
.PHONY: venv

venv:
	@poetry run poetry install

commit:
	@echo "Revisar mudanças para este commit: "
	@echo "-------------------------------------"
	@git status -s 
	@echo "-------------------------------------"
	@read -p "Mensagem do commit: " menssagem ; \
	git add . ;\
	git commit -m "$$menssagem" ;\

update:
	@git fetch origin
	@git pull
	@$(MAKE) venv