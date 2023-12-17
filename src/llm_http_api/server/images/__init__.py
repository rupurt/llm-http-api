from llm_http_api.server.fastapi import app


@app.post("/v1/images/generations")
async def create_image():
    return {"message": "TODO#POST create image"}


@app.post("/v1/images/edits")
async def create_image_edit():
    return {"message": "TODO#POST create image edit"}


@app.post("/v1/images/variations")
async def create_image_variation():
    return {"message": "TODO#POST create image variation"}
