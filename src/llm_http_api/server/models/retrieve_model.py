import llm
from typing import Set
from pydantic import BaseModel
from llm_http_api.server.fastapi import app


class ModelResult(BaseModel):
    id: str
    object: str = "model"
    # created: int
    # owned_by: str
    # aliases: Set[str]
    can_stream: bool


@app.get("/v1/models/{name}")
async def retrieve_model(name: str):
    model = llm.get_model(name)
    result = ModelResult(
        id=model.model_id,
        # created=0,
        # owned_by="todo",
        # aliases=[],
        can_stream=model.can_stream,
    )
    # embedding_models = llm.get_embedding_models_with_aliases()
    # print(embedding_models)
    return result
