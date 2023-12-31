from llm import hookimpl
import click
from llm_http_api.server import run, ServerSettings


@hookimpl
def register_commands(cli):
    @cli.command(name="http-api")
    @click.option("-h", "--host", type=str, default="0.0.0.0", show_default=True)
    @click.option("-p", "--port", type=int, default=8080, show_default=True)
    @click.option("-l", "--log-level", type=str, default="info", show_default=True)
    @click.option("-r", "--reload", is_flag=True, default=False, show_default=True)
    @click.option(
        "-d", "--reload-dirs", type=list[str], default=["src"], show_default=True
    )
    def http_api(
        host: str,
        port: int,
        log_level: str,
        reload: bool,
        reload_dirs: list[str],
    ):
        "Run a FastAPI HTTP server with OpenAI compatibility"
        run(
            ServerSettings(
                host=host,
                port=port,
                log_level=log_level,
                reload=reload,
                reload_dirs=reload_dirs,
            )
        )
