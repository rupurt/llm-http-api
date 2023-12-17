from llm_http_api.server.fastapi import app


@app.get("/v1/models")
async def list_models():
    return {"message": "TODO#GET models"}


@app.get("/v1/models/{model}")
async def retrieve_model():
    return {"message": "TODO#GET retrieve model"}


@app.delete("/v1/models/{model}")
async def delete_model():
    return {"message": "TODO#GET delete model"}
