from datetime import datetime
from llm_http_api.server.fastapi import app


@app.get("/probes/live")
async def probes_live():
    return {"now": datetime.now()}
