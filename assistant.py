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

    def create_assistant(self):
        self.client.beta.assistants.create()

    def get_assistant(self, assistant_id):
        return self.client.beta.assistants.retrieve(
            assistant_id=assistant_id,
        )

    def send_message(self, thread_id, content, role="user"):
        return

    def retrieve_messages(
        self,
    ):
        return
