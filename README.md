# llm-http-api

HTTP API for [LLM](https://github.com/simonw/llm) with OpenAI compatibility

## Usage

```shell
> llm http-api --help
Usage: llm http-api [OPTIONS]

  Run a FastAPI HTTP server with OpenAI compatibility

Options:
  -h, --host TEXT       [default: 0.0.0.0]
  -p, --port INTEGER    [default: 8080]
  -l, --log-level TEXT  [default: info]
  --help                Show this message and exit.
```

```shell
> curl http://localhost:8080/v1/embeddings -X POST -H "Content-Type: application/json" -d '{
  "input": "Hello world",
  "model": "jina-embeddings-v2-small-en"
}'
{"object":"embedding","embedding":[-0.47561466693878174,-0.4471365511417389,...],"index":0}
```

## OpenAI Endpoints

### Embeddings

- [x] [`POST /v1/embeddings`](./docs/endpoints/EMBEDDINGS.md)

### Unimplemented

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
