from llm_http_api.server.fastapi import app


@app.post("/v1/embeddings")
async def create_embedding():
    return {"message": "TODO#POST embedding"}
