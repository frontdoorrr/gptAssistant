import os
import json
from typing import Any, AnyStr, Dict

import openai


def get_json(setting: AnyStr, secrets: Dict) -> Any:
    return secrets[setting]


class GPTAssistant:
    def __init__(self) -> None:
        self.client = ""
        pass

    def create_assistant(
        self,
        name,
        instructions,
        tools=[{"type": "retrieval"}, {"type": "code_interpreter"}],
    ):
        self.client.beta.assistants.create(
            name=name,
            instructions=instructions,
            tools=tools,
        )

    def get_assistant(self, assistant_id):
        return self.client.beta.assistants.retrieve(
            assistant_id=assistant_id,
        )

    def send_message(
        self,
        thread_id,
        content,
        role="user",
    ):
        message = self.client.beta.threads.messages.create(
            thread_id=thread_id,
            content=content,
            role=role,
        )
        return message

    def retrieve_messages(
        self,
        thread_id,
        run_id,
    ):
        run = self.client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id,
        )
        return run
