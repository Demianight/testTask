venv:
	python3 -m venv venv

install:
	pip install -r requirements.txt

dmongo:
	docker run -d -p 27017:27017 --name db_mongo mongo

connect_mongo:
	docker exec -it db_mongo mongosh

run:
	python3 manage.py runserver

loaddata:
	python3 manage.py loaddata fixtures/fixtures.json 

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

createsuperuser:
	python3 manage.py createsuperuser

test:
	python3 manage.py test

linter:
	isort .
	flake8