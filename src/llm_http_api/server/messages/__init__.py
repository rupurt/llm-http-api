from llm_http_api.server.fastapi import app


@app.post("/v1/threads/{thread_id}/messages")
async def create_message():
    return {"message": "TODO#POST create message"}


@app.get("/v1/threads/{thread_id}/messages")
async def list_messages():
    return {"message": "TODO#GET list messages"}


@app.get("/v1/threads/{thread_id}/messages/{message_id}")
async def retrieve_message():
    return {"message": "TODO#GET retrieve message"}


@app.get("/v1/threads/{thread_id}/messages/{message_id}")
async def modify_message():
    return {"message": "TODO#POST modify message"}


@app.get("/v1/threads/{thread_id}/messages/{message_id}/files")
async def list_message_files():
    return {"message": "TODO#GET list message files"}


@app.get("/v1/threads/{thread_id}/messages/{message_id}/files/{file_id}")
async def retrieve_message_file():
    return {"message": "TODO#GET retrieve message file"}
