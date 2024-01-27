RUN=docker compose run --rm broker
all:
	docker compose build

run:
	docker compose up

migrations:
	$(RUN) python3 manage.py makemigrations

migrate:
	$(RUN) python3 manage.py migrate

shell:
	$(RUN) /bin/bash


fmt:
	$(RUN) poetry run black .
	$(RUN) poetry run isort . --profile black

lint:
	$(RUN) poetry run black . --check
	$(RUN) poetry run isort . -c --profile black

test:
	$(RUN) pytest -x -vvv --pdb
