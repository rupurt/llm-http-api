from llm_http_api.server.fastapi import app


@app.post("/v1/moderations")
async def create_moderation():
    return {"message": "TODO#POST create moderation"}
