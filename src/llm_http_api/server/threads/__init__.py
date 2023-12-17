from llm_http_api.server.fastapi import app


@app.post("/v1/threads")
async def create_thread():
    return {"message": "TODO#POST create thread"}


@app.get("/v1/threads/{thread_id}")
async def retrieve_thread():
    return {"message": "TODO#GET retrieve thread"}


@app.post("/v1/threads/{thread_id}")
async def modify_thread():
    return {"message": "TODO#POST modify thread"}


@app.delete("/v1/threads/{thread_id}")
async def delete_thread():
    return {"message": "TODO#DELETE thread"}
