from hamcrest import assert_that, is_not, empty, has_entries
from fastapi.testclient import TestClient
from llm_http_api.server.fastapi import app

client = TestClient(app)


def test_create_chat_completion():
    response = client.post(
        "/v1/chat/completions",
        json={
            "model": "mpt-7b-chat-merges-q4_0",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"},
            ],
        },
    )
    assert response.status_code == 200
    assert_that(
        response.json(),
        # TODO:
        # - assert on contents
        is_not(empty()),
    )
