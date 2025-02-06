migrate:
	python core/manage.py migrate

migrations:
	python core/manage.py makemigrations

db-update:
	make migrations
	make migrate

run:
	python core/manage.py runserver

new-app:
	python scripts/commands.py create_app

run-config:
	make db-update
	python scripts/commands.py create_local_superuser
	make run