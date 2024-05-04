run:
	python src/main.py /tmp/contacts.test.sqlite3

test:
	python -m unittest discover -s tests

