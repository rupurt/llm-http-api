from llm_http_api.server.fastapi import app


@app.post("/v1/chat/completions")
async def create_chat_completion():
    return {"message": "TODO#POST chat completion"}
