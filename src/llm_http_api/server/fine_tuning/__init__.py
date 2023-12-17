from llm_http_api.server.fastapi import app


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
