.PHONY: start
start:
	- docker-compose up -d
	- make migrate

.PHONY: stop
stop:
	docker-compose down

.PHONY: logs
logs:
	docker-compose logs

.PHONY: makemigrations
makemigrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: runserver
runserver:
	- python manage.py runserver

.PHONY: format
format:
	- black links/

.PHONY: format-check
format-check:
	- black --check links/
	- flake8 links/