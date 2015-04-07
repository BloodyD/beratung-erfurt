
start:
	python manage.py runserver

test:
	python manage.py test

resetdb:
	python manage.py reset_db
	python manage.py syncdb
	python manage.py migrate
	python manage.py loaddata dev_data.yaml