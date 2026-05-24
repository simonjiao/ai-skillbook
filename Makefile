.PHONY: new catalog check

TYPE ?= tool
SLUG ?=
TITLE ?=

new:
	python3 scripts/new_entry.py --type "$(TYPE)" --slug "$(SLUG)" --title "$(TITLE)"

catalog:
	python3 scripts/generate_catalog.py

check:
	python3 scripts/check_md_links.py
	python3 scripts/generate_catalog.py --check
