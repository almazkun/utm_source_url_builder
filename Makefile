run:
	pipenv run python manage.py runserver

mgrt:
	pipenv run python manage.py makemigrations
	pipenv run python manage.py migrate

lint:
	pipenv run isort --recursive --force-single-line-imports --line-width 999 .
	pipenv run autoflake --recursive --ignore-init-module-imports --in-place --remove-all-unused-imports .
	pipenv run isort --recursive --use-parentheses --trailing-comma --multi-line 3 --force-grid-wrap 0 --line-width 88 .
	pipenv run black .

test:
	pipenv run coverage run manage.py test
	pipenv run coverage report -m