from llm_http_api.server.fastapi import app


@app.post("/v1/assistants")
async def create_assistant():
    return {"message": "TODO#POST create assistant"}


@app.get("/v1/assistants")
async def list_assistants():
    return {"message": "TODO#GET list assistants"}


@app.get("/v1/assistants/{assistant_id}")
async def retrieve_assistant():
    return {"message": "TODO#GET retrieve assistant"}


@app.post("/v1/assistants/{assistant_id}")
async def modify_assistant():
    return {"message": "TODO#POST modify assistant"}


@app.delete("/v1/assistants/{assistant_id}")
async def delete_assistant():
    return {"message": "TODO#DELETE assistant"}


@app.post("/v1/assistants/{assistant_id}/files")
async def create_assistant_file():
    return {"message": "TODO#POST create assistant file"}


@app.get("/v1/assistants/{assistant_id}/files")
async def list_assistant_file():
    return {"message": "TODO#GET list assistant file"}


@app.get("/v1/assistants/{assistant_id}/files/{file_id}")
async def retrieve_assistant_file():
    return {"message": "TODO#GET retrieve assistant file"}


@app.delete("/v1/assistants/{assistant_id}/files/{file_id}")
async def delete_assistant_file():
    return {"message": "TODO#DELETE assistant file"}
