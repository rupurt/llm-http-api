from fastapi.responses import RedirectResponse
from llm_http_api.server.fastapi import app


@app.get("/")
async def root():
    return RedirectResponse("/docs")
