# Endpoints/Models

### Model object

[OpenAI reference](https://platform.openai.com/docs/api-reference/models/object)

- `id` - string
- `created` - integer - Not supported
- `object` - string
- `owned_by` - string - Not supported
- `aliases` - array of strings - LLM addition
- `can_stream` - boolean - LLM addition

## `GET` /v1/models

[OpenAI reference](https://platform.openai.com/docs/api-reference/models/list)

### Returns

A list of [model objects](#model-object).

### Example

```shell
> curl http://localhost:8080/v1/models
{"object":"list","data":[{"id":"gpt-3.5-turbo","object":"model","aliases":["3.5","chatgpt"],"can_stream":true},...]}
```

## `GET` /v1/models/{model}

[OpenAI reference](https://platform.openai.com/docs/api-reference/models/retrieve)

### Path parameters

- `model` - string - Required

### Returns

The [model object](#model-object) matching the specified id or alias

### Example

```shell
> curl http://localhost:8080/v1/models/gpt-4
{"id":"gpt-4","object":"model","can_stream":true}
```

## `DELETE` /v1/models/{model}

Not supported
