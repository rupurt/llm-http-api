import llm
from typing import Optional
from pydantic import BaseModel
from llm_http_api.server.fastapi import app


class Embed(BaseModel):
    # input: str | list[str] | bytes | list[bytes]
    input: str | bytes
    model: str
    encoding_format: Optional[str] = "float"
    user: Optional[str] = None


class EmbeddingResult(BaseModel):
    object: str = "embedding"
    embedding: list[float]
    index: int


@app.post("/v1/embeddings")
async def create_embedding(embed: Embed):
    model = llm.get_embedding_model(embed.model)
    embedding = model.embed(embed.input)
    return EmbeddingResult(
        object="embedding",
        embedding=embedding,
        index=0,
    )
