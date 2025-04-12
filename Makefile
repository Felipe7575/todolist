# Variables
DOCKER=docker-compose run --rm web

# Comandos
up:
	docker-compose up

build:
	docker-compose build

migrate:
	$(DOCKER) python manage.py migrate

makemigrations:
	$(DOCKER) python manage.py makemigrations

createsuperuser:
	$(DOCKER) python manage.py createsuperuser

test:
	$(DOCKER) pytest

lint:
	flake8

format:
	black .

shell:
	$(DOCKER) python manage.py shell

down:
	docker-compose down --remove-orphans
