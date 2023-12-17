all: deps.install deps.install/test lint test coverage

deps.install:
	pip install -e .
deps.install/test:
	pip install -e ".[test]"
deps.freeze:
	python -m pip freeze > requirements.txt
deps.freeze/test:
	python -m pip freeze > requirements.test.txt
deps.reqs:
	pipreqs . --savepath requirements.txt
deps.reqs/test:
	pipreqs . --savepath requirements.test.txt
deps/outdated:
	python -m pip list --outdated
deps/check:
	python -m pip check

format:
	python -m ruff format .

lint:
	python -m ruff check .

test:
	pytest src

coverage:
	pytest --cov src

publish/pypi:
	python3 -m build && \
		python3 -m twine upload --repository pypi dist/*
