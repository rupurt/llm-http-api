# llm-http-api

HTTP API for [LLM](https://github.com/simonw/llm) with OpenAI compatibility

## Install

```shell
> pip install llm
> pip install llm-http-api
```

## Getting Started

1. Follow the [directions](https://github.com/simonw/llm?tab=readme-ov-file#getting-started) from LLM
2. Run the plugin `llm http-api`
3. Visit the OpenAPI documentation [localhost:8080/docs](http://localhost:8080/docs)

## Usage

```shell
> llm http-api --help
Usage: llm http-api [OPTIONS]

  Run a FastAPI HTTP server with OpenAI compatibility

Options:
  -h, --host TEXT         [default: 0.0.0.0]
  -p, --port INTEGER      [default: 8080]
  -l, --log-level TEXT    [default: info]
  -r, --reload
  -d, --reload-dirs LIST  [default: src]
  --help                  Show this message and exit.
```

```shell
> curl http://localhost:8080/v1/embeddings -X POST -H "Content-Type: application/json" -d '{
  "input": "Hello world",
  "model": "jina-embeddings-v2-small-en"
}'
{"object":"embedding","embedding":[-0.47561466693878174,-0.4471365511417389,...],"index":0}
```

## Supported OpenAI Endpoints

### Models

- [x] [`GET /v1/models`](./docs/endpoints/MODELS.md)
- [x] [`GET /v1/models/{model}`](./docs/endpoints/MODELS.md)
- [ ] [`DELETE /v1/models/{model}`](./docs/endpoints/MODELS.md)

### Embeddings

- [x] [`POST /v1/embeddings`](./docs/endpoints/EMBEDDINGS.md)

### Chat

- [ ] [`POST /v1/chat/completions`](./docs/endpoints/CHAT.md)

## Unsupported OpenAI Endpoints

A detailed list of unimplemented OpenAI endpoints can be found [here](./docs/endpoints/UNIMPLEMENTED.md)

## Development

This repository manages the dev environment as a Nix flake and requires [Nix to be installed](https://github.com/DeterminateSystems/nix-installer)

```shell
nix develop -c $SHELL
```

```shell
make deps.install
make deps.install/test
```

```shell
make run/dev
```

```shell
make test
```

```shell
make coverage
```

```shell
make lint
```

```shell
make format
```

## Publish Package to PyPi

```shell
make publish/pypi
```

## Local LLM's

```shell
make llm.setup/mlc
make llm.mlc.download/code_llama-34b-python-q4f16
make llm.mlc.download/code_llama-34b-instruct-q0f16
make llm.mlc.download/code_llama-13b-q4f16
make llm.mlc.download/code_llama-7b-q4f16
make llm.mlc.download/wizard-coder-15b-q4f32
make llm.mlc.download/open_hermes-2.5-mistral-7b-q4f16
make llm.mlc.download/mistral-7b-instruct-q4f16
```
