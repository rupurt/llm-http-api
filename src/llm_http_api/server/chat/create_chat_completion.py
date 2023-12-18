import llm
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from llm_http_api.server.fastapi import app


class Message(BaseModel):
    role: str
    content: str


class ChatCompletion(BaseModel):
    model: str
    messages: list[Message]


class LogProbs(BaseModel):
    content: Optional[list[str]]


class ChatCompletionChoice(BaseModel):
    finish_reason: str
    index: int
    message: str
    logprobs: Optional[LogProbs] = None


class ChatCompletionUsage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatCompletionResult(BaseModel):
    id: str = "todo"
    object: str = "chat.completion"
    created: int
    model: str
    system_fingerprint: str = "todo"
    choices: list[ChatCompletionChoice]
    usage: ChatCompletionUsage


def prompt_model(model, prompt):
    response = model.prompt(prompt)
    return ChatCompletionChoice(
        finish_reason="todo",
        index=0,
        message=response.text(),
    )


def chat_choices(model, messages):
    choices = []
    i = 0
    for msg in messages:
        # choice = prompt_model(model, message.content)
        response = model.prompt(msg.content)
        choice = ChatCompletionChoice(
            finish_reason="todo",
            index=i,
            message=response.text(),
        )
        choices.append(choice)
        i += 1
    return choices


@app.post("/v1/chat/completions")
async def create_chat_completion(chat: ChatCompletion):
    model = llm.get_model(chat.model)
    # choices = list(map(lambda m: prompt_model(model, m.content), chat.messages))
    choices = chat_choices(model, chat.messages)
    created_at = int(round(datetime.utcnow().timestamp()))
    return ChatCompletionResult(
        created=created_at,
        model=chat.model,
        choices=choices,
        usage=ChatCompletionUsage(
            prompt_tokens=0,
            completion_tokens=0,
            total_tokens=0,
        ),
    )
