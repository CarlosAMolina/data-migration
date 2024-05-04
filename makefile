export:
	python src/main.py /tmp/contacts.sqlite3

import:
	python src/main.py /tmp/contacts.sqlite3-20240504131728/ /tmp/contacts.sqlite3

test:
	python -m unittest discover -s tests

