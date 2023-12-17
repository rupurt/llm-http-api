from hamcrest import assert_that, is_not, empty, has_entries
from fastapi.testclient import TestClient
from llm_http_api.server.fastapi import app

client = TestClient(app)


def test_create_embedding():
    response = client.post(
        "/v1/embeddings",
        json={
            "input": "Hello World",
            "model": "jina-embeddings-v2-small-en",
        },
    )
    assert response.status_code == 200
    assert_that(
        response.json(),
        has_entries(
            {
                "object": "embedding",
                "embedding": is_not(empty()),
                "index": 0,
            }
        ),
    )
