from llm_http_api.server.fastapi import app


@app.post("/v1/audio/speech")
async def create_speech():
    return {"message": "TODO#POST speech"}


@app.post("/v1/audio/transcriptions")
async def create_transcription():
    return {"message": "TODO#POST transcription"}


@app.post("/v1/audio/translations")
async def create_translation():
    return {"message": "TODO#POST translations"}
