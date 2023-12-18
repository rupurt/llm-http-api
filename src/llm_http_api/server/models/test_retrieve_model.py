from hamcrest import assert_that, is_not, empty, has_entries
from fastapi.testclient import TestClient
from llm_http_api.server.fastapi import app

client = TestClient(app)


def test_retrieve_model():
    response = client.get("/v1/models/gpt-4")
    assert response.status_code == 200
    assert_that(
        response.json(),
        has_entries(
            {
                "id": "gpt-4",
                "object": "model",
                # "aliases": ["gpt4", "4"],
            }
        ),
    )
