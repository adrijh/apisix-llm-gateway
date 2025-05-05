import requests
from openai import OpenAI

ENDPOINT = "http://127.0.0.1:9080"
HEADERS = {"Content-Type": "application/json"}


def build_messages(question: str) -> list[dict[str, str]]:
    return [
        { "role": "system", "content": "You are an assistant." },
        { "role": "user", "content": question },
    ]

def ask_with_requests(route_name: str, question: str, headers: dict[str, str]) -> str:
    messages = build_messages(question)
    payload = {"messages": messages}
    response = requests.post(f"{ENDPOINT}/{route_name}", json=payload, headers=headers)
    return response.json()["choices"][0]["message"]["content"]


def ask_with_openai(route_name: str, question: str, extra_headers: dict[str, str] | None = None) -> str:
    client = OpenAI(
        base_url=f"{ENDPOINT}/{route_name}",
        api_key="does not matter"
    )

    messages = build_messages(question)
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages, # type: ignore
        extra_headers=extra_headers,
    )
    choice = completion.choices[0] if completion.choices else None
    if not choice or not choice.message.content:
        raise Exception

    return choice.message.content
