run:
	python src/sqlite.py /tmp/contacts.test.sqlite3

test:
	python -m unittest discover -s tests

