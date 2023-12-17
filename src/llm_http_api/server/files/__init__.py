from llm_http_api.server.fastapi import app


@app.post("/v1/files")
async def create_file():
    return {"message": "TODO#POST file"}


@app.get("/v1/files")
async def list_files():
    return {"message": "TODO#GET list files"}


@app.get("/v1/files/{file_id}")
async def retrieve_file():
    return {"message": "TODO#GET file"}


@app.delete("/v1/files/{file_id}")
async def delete_file():
    return {"message": "TODO#DELETE file"}


@app.get("/v1/files/{file_id}/content")
async def retrieve_file_content():
    return {"message": "TODO#GET file content"}
