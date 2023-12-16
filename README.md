# llm-http-api

HTTP API for [LLM](https://github.com/simonw/llm) with OpenAI compatibility

## Usage

```shell
Usage: llm http-api [OPTIONS]

  Run a FastAPI HTTP server with OpenAI compatibility

Options:
  -h, --host TEXT       [default: 0.0.0.0]
  -p, --port INTEGER    [default: 8080]
  -l, --log-level TEXT  [default: info]
  --help                Show this message and exit.
```

## OpenAI Endpoints

### Audio

- [ ] `POST /v1/audio/speech`
- [ ] `POST /v1/audio/transcriptions`
- [ ] `POST /v1/audio/translations`

### Chat

- [ ] `POST /v1/chat/completions`

### Embeddings

- [ ] `POST /v1/embeddings`

### Fine Tuning

- [ ] `POST /v1/fine_tuning/jobs`
- [ ] `GET /v1/fine_tuning/jobs`
- [ ] `GET /v1/fine_tuning/jobs/{fine_tuning_job_id}`
- [ ] `POST /v1/fine_tuning/jobs/{fine_tuning_job_id}/cancel`
- [ ] `GET /v1/fine_tuning/jobs/{fine_tuning_job_id}/events`

### Files

- [ ] `POST /v1/files`
- [ ] `GET /v1/files`
- [ ] `GET /v1/files/{file_id}`
- [ ] `DELETE /v1/files/{file_id}`
- [ ] `GET /v1/files/{file_id}/content`

### Images

- [ ] `POST /v1/images/generations`
- [ ] `POST /v1/images/edit`
- [ ] `POST /v1/images/variations`

### Models

- [ ] `GET /v1/models`
- [ ] `GET /v1/models/{model}`
- [ ] `DELETE /v1/models/{model}`

### Moderations

- [ ] `POST /v1/moderations`
- [ ] `GET /v1/models/{model}`

### Assistants

- [ ] `POST /v1/assistants`
- [ ] `GET /v1/assistants`
- [ ] `GET /v1/assistants/{assistant_id}`
- [ ] `POST /v1/assistants/{assistant_id}`
- [ ] `DELETE /v1/assistants/{assistant_id}`
- [ ] `POST /v1/assistants/{assistant_id}/files`
- [ ] `GET /v1/assistants/{assistant_id}/files`
- [ ] `GET /v1/assistants/{assistant_id}/files/{file_id}`
- [ ] `DELETE /v1/assistants/{assistant_id}/files/{file_id}`

### Threads

- [ ] `POST /v1/threads`
- [ ] `GET /v1/threads/{thread_id}`
- [ ] `POST /v1/threads/{thread_id}`
- [ ] `DELETE /v1/threads/{thread_id}`

### Messages

- [ ] `POST /v1/threads/{thread_id}/messages`
- [ ] `GET /v1/threads/{thread_id}/messages`
- [ ] `GET /v1/threads/{thread_id}/messages/{message_id}`
- [ ] `POST /v1/threads/{thread_id}/messages/{message_id}`
- [ ] `GET /v1/threads/{thread_id}/messages/{message_id}/files`
- [ ] `GET /v1/threads/{thread_id}/messages/{message_id}/files/{file_id}`

### Runs

- [ ] `POST /v1/threads/{thread_id}/runs`
- [ ] `GET /v1/threads/{thread_id}/runs`
- [ ] `GET /v1/threads/{thread_id}/runs/{run_id}`
- [ ] `POST /v1/threads/{thread_id}/runs/{run_id}`
- [ ] `POST /v1/threads/{thread_id}/runs/{run_id}/submit_tool_outputs`
- [ ] `POST /v1/threads/{thread_id}/runs/{run_id}/cancel`
- [ ] `POST /v1/threads/run`
- [ ] `GET /v1/threads/{thread_id}/runs/{run_id}/steps/{step_id}`
- [ ] `GET /v1/threads/{thread_id}/runs/{run_id}/steps`

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
