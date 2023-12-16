from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.openapi.docs import (
    get_swagger_ui_html,
)
from pydantic_settings import (
    BaseSettings,
)
from datetime import datetime
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse("/docs")


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url or "/docs",
        title=app.title + " - Swagger UI",
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui.css",
    )


@app.get("/probes/live")
async def probes_live():
    return {"now": datetime.now()}


@app.post("/v1/audio/speech")
async def create_speech():
    return {"message": "TODO#POST speech"}


@app.post("/v1/audio/transcriptions")
async def create_transcription():
    return {"message": "TODO#POST transcription"}


@app.post("/v1/audio/translations")
async def create_translation():
    return {"message": "TODO#POST translations"}


@app.post("/v1/chat/completions")
async def create_chat_completion():
    return {"message": "TODO#POST chat completion"}


@app.post("/v1/embeddings")
async def create_embedding():
    return {"message": "TODO#POST embedding"}


@app.post("/v1/fine_tuning/jobs")
async def create_fine_tuning_job():
    return {"message": "TODO#POST fine tuning job"}


@app.get("/v1/fine_tuning/jobs")
async def list_fine_tuning_jobs():
    return {"message": "TODO#GET list fine tuning jobs"}


@app.get("/v1/fine_tuning/jobs/{fine_tuning_job_id}")
async def show_fine_tuning_job():
    return {"message": "TODO#GET fine tuning job by id"}


@app.post("/v1/fine_tuning/jobs/{fine_tuning_job_id}/cancel")
async def cancel_fine_tuning_job():
    return {"message": "TODO#POST cancel fine tuning job"}


@app.get("/v1/fine_tuning/jobs/{fine_tuning_job_id}/events")
async def list_fine_tuning_job_events():
    return {"message": "TODO#GET list fine tuning job events"}


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


@app.post("/v1/images/generations")
async def create_image():
    return {"message": "TODO#POST create image"}


@app.post("/v1/images/edits")
async def create_image_edit():
    return {"message": "TODO#POST create image edit"}


@app.post("/v1/images/variations")
async def create_image_variation():
    return {"message": "TODO#POST create image variation"}


@app.get("/v1/models")
async def list_models():
    return {"message": "TODO#GET models"}


@app.get("/v1/models/{model}")
async def retrieve_model():
    return {"message": "TODO#GET retrieve model"}


@app.delete("/v1/models/{model}")
async def delete_model():
    return {"message": "TODO#GET delete model"}


@app.post("/v1/moderations")
async def create_moderation():
    return {"message": "TODO#POST create moderation"}


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


@app.post("/v1/threads/runs")
async def create_thread_and_run():
    return {"message": "TODO#POST create thread run"}


@app.post("/v1/threads/{thread_id}/runs")
async def create_thread_run():
    return {"message": "TODO#POST create run"}


@app.get("/v1/threads/{thread_id}/runs")
async def list_thread_runs():
    return {"message": "TODO#GET list runs"}


@app.get("/v1/threads/{thread_id}/runs/{run_id}")
async def retrieve_thread_run():
    return {"message": "TODO#GET retrieve run"}


@app.post("/v1/threads/{thread_id}/runs/{run_id}")
async def modify_thread_run():
    return {"message": "TODO#POST modify run"}


@app.post("/v1/threads/{thread_id}/runs/{run_id}/submit_tool_outputs")
async def submit_tool_outputs_to_thread_run():
    return {"message": "TODO#POST submit tool outputs to run"}


@app.post("/v1/threads/{thread_id}/runs/{run_id}/cancel")
async def cancel_thread_run():
    return {"message": "TODO#POST cancel run"}


@app.get("/v1/threads/{thread_id}/runs/{run_id}/steps")
async def list_thread_run_steps():
    return {"message": "TODO#GET list run steps"}


@app.get("/v1/threads/{thread_id}/runs/{run_id}/steps/{step_id}")
async def retrieve_thread_run_step():
    return {"message": "TODO#GET retrieve run step"}


class ServerSettings(BaseSettings):
    host: str
    port: int
    log_level: str


def run(settings: ServerSettings):
    uvicorn.run(
        app, host=settings.host, port=settings.port, log_level=settings.log_level
    )
