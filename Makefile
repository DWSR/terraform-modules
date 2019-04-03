.SILENT:

default: docs lint

init:
	python3 -m venv .venv
	.venv/bin/pip3 install -r requirements.txt

docs:
	python3 ./scripts/gen_docs.py

lint:
	python3 ./scripts/lint.py

install-hooks:
	cp -p ./scripts/pre-commit.sh ./.git/hooks/pre-commit
