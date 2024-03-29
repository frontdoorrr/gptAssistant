import os
import json

import openai


secretpath = "info.json"
with open(secretpath) as f:
    secrets = json.loads(f.read())


def get_json(setting, secrets=secrets):
    return secrets[setting]


OPENAI_API_KEY = get_json("OPENAI_API_KEY")
FILE_PATHS = get_json("FILE_PATHS")
FILE_PATHS = FILE_PATHS.split(",")

client = openai.OpenAI(api_key=OPENAI_API_KEY)


# # class GPTClient:
# #     def __init__(self, api_key) -> None:
# #         self.api_key = api_key
# #         self.client = openai.OpenAI()

# #     def _create_assistant(self):
# #         return

# #     def _create_thread(self):
# #         return

# #     def _create_messeage(self):
# #         return

# #     def _receive_message(self):
# #         self.client

# File upload
file_ids = []
for filepath in FILE_PATHS:
    file = client.files.create(
        file=open(filepath, "rb"),
        purpose="assistants",
    )
    file_ids.append(file.id)
print("*****", file_ids)


assistant = client.beta.assistants.create(
    name="커피 테스트 Assistant",
    instructions="커피 원두와 관련된 정보를 알려줍니다.",
    tools=[
        {
            "type": "retrieval",
        },
        {
            "type": "code_interpreter",
        },
    ],
    file_ids=file_ids,
    model="gpt-4-1106-preview",
)

print(type(assistant), assistant)


# Create thread
thread = client.beta.threads.create()
print("Thread :", thread)
# Create Message

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    content="가성비가 좋은 원두에 대해 알려주세요",
    # file_ids=file_ids,
    role="user",
)

print("Message :", message)
# Create Response

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
)
print("Run :", run)

# Print Response

run = client.beta.threads.runs.retrieve(
    thread_id=thread.id,
    run_id=run.id,
)

print("Run :", run)

messages = client.beta.threads.messages.list(thread_id=thread.id)
print("Messages  : ", messages)
# message = [message.content[0].text for message in messages if message.run_id == run.id][
#     0
# ]


for message in reversed(messages.data):
    print(message.role + " : ", message.content[0].text.value)
# messages.data[0].content
