from pydantic_settings import (
    BaseSettings,
)
import uvicorn
import importlib

importlib.import_module("llm_http_api.server.root")
importlib.import_module("llm_http_api.server.swagger")
importlib.import_module("llm_http_api.server.probes")
importlib.import_module("llm_http_api.server.audio")
importlib.import_module("llm_http_api.server.chat")
importlib.import_module("llm_http_api.server.embeddings")
importlib.import_module("llm_http_api.server.fine_tuning")
importlib.import_module("llm_http_api.server.files")
importlib.import_module("llm_http_api.server.images")
importlib.import_module("llm_http_api.server.models")
importlib.import_module("llm_http_api.server.moderations")
importlib.import_module("llm_http_api.server.assistants")
importlib.import_module("llm_http_api.server.threads")
importlib.import_module("llm_http_api.server.messages")
importlib.import_module("llm_http_api.server.runs")


class ServerSettings(BaseSettings):
    host: str
    port: int
    log_level: str
    reload: bool
    reload_dirs: list[str]


def run(settings: ServerSettings):
    uvicorn.run(
        "llm_http_api.server.fastapi:app",
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level,
        reload=settings.reload,
        reload_dirs=settings.reload_dirs,
    )
