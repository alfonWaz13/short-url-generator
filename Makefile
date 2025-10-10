.PHONY: run-local
run-local:
	- make run-local-db
	- sleep 2
	- make migrate
	- python manage.py runserver

.PHONY: run-production
run-production:
	- make migrate
	- gunicorn --workers 3 --bind 0.0.0.0:8000 url_shortener.wsgi:application

.PHONY: stop
stop:
	docker-compose down

.PHONY: run-local-db
run-local-db:
	docker-compose up -d

.PHONY: logs
logs:
	docker-compose logs

.PHONY: makemigrations
makemigrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: format
format:
	black links/

.PHONY: format-check
format-check:
	- black --check links/
	- flake8 links/