export-postgresql:
	python src/main.py postgresql

export-sqlite:
	python src/main.py sqlite /tmp/contacts.sqlite3

import-sqlite:
	python src/main.py sqlite /tmp/contacts.sqlite3-20240504131728/ /tmp/contacts.sqlite3

test:
	python -m unittest discover -s tests

