import llm
from typing import Set
from pydantic import BaseModel
from llm_http_api.server.fastapi import app


class ModelResult(BaseModel):
    id: str
    object: str = "model"
    # created: int
    # owned_by: str
    aliases: Set[str]
    can_stream: bool


class ListModelsResult(BaseModel):
    object: str = "list"
    data: list[ModelResult]


@app.get("/v1/models")
async def list_models():
    models = llm.get_models_with_aliases()
    data = map(
        lambda m: ModelResult(
            id=m.model.model_id,
            # created=0,
            # owned_by="todo",
            aliases=m.aliases,
            can_stream=m.model.can_stream,
        ),
        models,
    )
    # embedding_models = llm.get_embedding_models_with_aliases()
    # print(embedding_models)
    return ListModelsResult(object="list", data=list(data))
