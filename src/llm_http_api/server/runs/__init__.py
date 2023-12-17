from llm_http_api.server.fastapi import app


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
