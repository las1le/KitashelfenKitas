default: live_test

venv:
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade setuptools && pip install -e .

live_test: venv
	. venv/bin/activate && pip -V && which python && python scripts/live_test.py

clean:
	rm -rf venv
	find . -type f -name '*.pyc' -delete

test: venv
	. venv/bin/activate && pip install pytest && pytest tests

.PHONY: all run clean test
