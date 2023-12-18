from hamcrest import assert_that, is_not, empty, has_entries
from fastapi.testclient import TestClient
from llm_http_api.server.fastapi import app

client = TestClient(app)


def test_list_models():
    response = client.get("/v1/models")
    assert response.status_code == 200
    assert_that(
        response.json(),
        has_entries(
            {
                "object": "list",
                "data": is_not(empty()),
            }
        ),
    )
