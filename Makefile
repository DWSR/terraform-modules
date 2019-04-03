.SILENT:

default: docs lint

docs:
	python3 ./scripts/gen_docs.py

lint:
	python3 ./scripts/lint.py

install-hooks:
	cp -p ./scripts/pre-commit.sh ./.git/hooks/pre-commit
