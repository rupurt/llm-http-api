# Endpoints/Chat

### Chat completion object

[OpenAI reference](https://platform.openai.com/docs/api-reference/chat/object)

- `id` - string
- `choices` - array
    - `finish_reason` - string
    - `index` - integer
    - `message` - object
    - `logprobs` - object or null
        - `content` - array or null
- `created` - integer
- `model` - string
- `system_fingerprint` - string
- `object` - string
- `usage` - object

### Chat completion chunk object

[OpenAI reference](https://platform.openai.com/docs/api-reference/chat/streaming)

- `id` - string
- `choices` - array
    - `finish_reason` - string
    - `index` - integer
    - `message` - object
    - `logprobs` - object or null
        - `content` - array or null
- `created` - integer
- `model` - string
- `system_fingerprint` - string
- `object` - string

## `POST` /v1/chat/completions

[OpenAI reference](https://platform.openai.com/docs/api-reference/chat/create)

### Request body

- `messages` - array - Required
- `model` - string - Required
- `frequency_penalty` - number or null - Optional - Defaults to 0
- `logit_bias` - map - Optional - Defaults to null
- `logprobs` - boolean or null - Optional - Defaults to false
- `top_logprobs` - integer or null - Optional
- `max_tokens` - integer or null - Optional
- `n` - integer or null - Optional - Defaults to 1
- `presence_penalty` - number or null - Optional - Defaults to 0
- `response_format` - object - Optional
- `seed` - integer or null - Optional
- `stop` - string / array / null - Optional - Defaults to null
- `stream` - boolean or null - Optional - Defaults to false
- `temperature` - number or null - Optional - Defaults to 1
- `top_p` - number or null - Optional - Defaults to 1
- `tools` - array - Optional
- `tool_choice` - string or object - Optional
- `user` - string - Optional
- `function_call` - Deprecated - string or object - Optional
- `functions` - Deprecated - array - Optional

### Returns

Returns a [chat completion object](#chat-completion-object), or a streamed sequence of
[chat completion chunk objects](#chat-completion-chunk-object) if the request is streamed.

### Example

```shell
> curl http://localhost:8080/v1/chat/completions -X POST -H "Content-Type: application/json" -d '{
  "model": "mpt-7b-chat-merges-q4_0",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "Hello!"
    }
  ]
}'
TODO...
```
