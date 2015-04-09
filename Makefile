
start:
	python manage.py runserver

test:
	python manage.py test

dump:
	python manage.py dumpdata beratung_erfurt --format=yaml > fixtures/current.yaml

current:
	python manage.py loaddata current.yaml

resetdb:
	python manage.py reset_db
	python manage.py syncdb
	python manage.py migrate
	python manage.py loaddata dev_data.yaml