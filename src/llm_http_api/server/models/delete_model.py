from llm_http_api.server.fastapi import app


@app.delete("/v1/models/{model}")
async def delete_model():
    return {"message": "TODO#GET delete model"}
