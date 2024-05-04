export:
	python src/main.py /tmp/contacts.sqlite3

test:
	python -m unittest discover -s tests

