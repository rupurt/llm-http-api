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

llm.setup/mlc:
  llm mlc pip install --pre --force-reinstall \
		mlc-ai-nightly \
		mlc-chat-nightly \
		-f https://mlc.ai/wheels

llm.mlc.download/code_llama-34b-python-q4f16:
	llm mlc download-model https://huggingface.co/mlc-ai/mlc-chat-CodeLlama-34b-Python-hf-q4f16_1 --alias code_llama-34b-python-q4f16
llm.mlc.download/code_llama-34b-instruct-q0f16:
	llm mlc download-model https://huggingface.co/mlc-ai/mlc-chat-CodeLlama-34b-Instruct-hf-q0f16 --alias code_llama-34b-instruct-q0f16
llm.mlc.download/code_llama-13b-q4f16:
	llm mlc download-model https://huggingface.co/mlc-ai/mlc-chat-CodeLlama-13b-hf-q4f16_1 --alias code_llama-13b-q4f16
llm.mlc.download/code_llama-7b-q4f16:
	llm mlc download-model https://huggingface.co/mlc-ai/mlc-chat-CodeLlama-7b-hf-q4f16_1 --alias code_llama-7b-q4f16
llm.mlc.download/wizard-coder-15b-q4f32:
	llm mlc download-model https://huggingface.co/mlc-ai/mlc-chat-WizardCoder-15B-V1.0-q4f32_1 --alias wizard-coder-15b-q4f16
llm.mlc.download/open_hermes-2.5-mistral-7b-q4f16:
	llm mlc download-model https://huggingface.co/mlc-ai/OpenHermes-2.5-Mistral-7B-q4f16_1-MLC --alias open-hermes-2.5-mistral-7b-q4f16
llm.mlc.download/mistral-7b-instruct-q4f16:
	llm mlc download-model https://huggingface.co/mlc-ai/mlc-chat-Mistral-7B-Instruct-v0.2-q4f16_1 --alias mistral-7b-instruct-q4f16
