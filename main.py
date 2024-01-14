import os

import openai

api_key = os.environ.get("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)


# class GPTClient:
#     def __init__(self, api_key) -> None:
#         self.api_key = api_key
#         self.client = openai.OpenAI()

#     def _create_assistant(self):
#         return

#     def _create_thread(self):
#         return

#     def _create_messeage(self):
#         return

#     def _receive_message(self):
#         self.client

assistant = client.beta.assistants.create(
    name="테스트 봇",
    instructions="개발 테스트를 위해 만들었습니다",
    tools=[
        {
            "type": "retrieval",
        }
    ],
    model="gpt-4-1106-preview",
)

print(type(assistant), assistant)

# File upload
file1 = client.files.create(file=open("", "rb"), purpose="assistants")
file2 = client.files.create(file=open("", "rb"), purpose="assistants")

# Create thread
thread = client.beta.threads.create()

# Create Message

message = client.beta.threads.messages.create()

# Create Response

run = client.beta.threads.run.create(thread_id=thread.id, assistant_id=assistant.id)
