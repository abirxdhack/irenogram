VENV := venv
PYTHON := $(VENV)/bin/python

RM := rm -rf

.PHONY: venv clean-docs docs

venv:
	$(RM) $(VENV)
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install -U pip wheel setuptools
	$(PYTHON) -m pip install -U -e .[docs]
	@echo "Created venv with $$($(PYTHON) --version)"

clean-docs:
	$(RM) docs/build
	$(RM) docs/source/api/bound-methods docs/source/api/methods docs/source/api/types docs/source/api/enums docs/source/telegram

docs:
	make clean-docs
	cd compiler/docs && ../../$(PYTHON) compiler.py
	$(VENV)/bin/sphinx-build \
		-b dirhtml "docs/source" "docs/build/html" -j auto
