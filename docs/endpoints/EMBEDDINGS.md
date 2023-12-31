# Endpoints/Embeddings

### Embedding object

[OpenAI reference](https://platform.openai.com/docs/api-reference/embeddings/object)

- `index` - integer
- `embedding` - array
- `object` - string

## `POST` /v1/embeddings

[OpenAI reference](https://platform.openai.com/docs/api-reference/embeddings)

### Request body

- `input` - string or array - Required
- `model` - string - Required
- `encoding_format` - string - Optional - Defaults to float
- `user` - string - Optional - Ignored

### Returns

A list of [embedding objects](#embedding-object).

### Example

```shell
> curl http://localhost:8080/v1/embeddings -X POST -H "Content-Type: application/json" -d '{
  "input": "Hello world",
  "model": "jina-embeddings-v2-small-en"
}'
{"object":"embedding","embedding":[-0.47561466693878174,-0.4471365511417389,...],"index":0}
```
