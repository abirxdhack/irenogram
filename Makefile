VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(PYTHON) -m pip

RM := rm -rf

.PHONY: venv venv-docs clean-venv clean-build clean-api clean-docs clean api docs docs-archive build

venv:
	@if [ ! -d "$(VENV)" ]; then \
		python3 -m venv $(VENV); \
		$(PIP) install -U pip wheel setuptools; \
	fi
	$(PIP) install -U -e .

venv-docs:
	@if [ ! -d "$(VENV)" ]; then \
		python3 -m venv $(VENV); \
		$(PIP) install -U pip wheel setuptools; \
	fi
	$(PIP) install -U -e .[docs]

clean-venv:
	$(RM) $(VENV)

clean-build:
	$(RM) *.egg-info build dist

clean-api:
	$(RM) pyrogram/errors/exceptions pyrogram/raw/all.py pyrogram/raw/base pyrogram/raw/functions pyrogram/raw/types

clean-docs:
	$(RM) docs/build docs/source/api/bound-methods docs/source/api/methods docs/source/api/types docs/source/api/enums docs/source/telegram

clean: clean-venv clean-build clean-api clean-docs

api:
	cd compiler/api && ../../$(PYTHON) compiler.py
	cd compiler/errors && ../../$(PYTHON) compiler.py

docs:
	cd compiler/docs && ../../$(PYTHON) compiler.py
	$(VENV)/bin/sphinx-build -b dirhtml "docs/source" "docs/build/html" -j auto

docs-archive:
	cd docs/build/html && zip -r ../docs.zip ./

build:
	hatch build
