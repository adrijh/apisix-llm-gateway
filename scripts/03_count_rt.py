from common import ask_with_openai

ROUTE_NAME = "countrt"
QUESTION = "What is 1 + 1?"
HEADERS_WITH_KEY = {
    "Content-Type": "application/json",
    "apikey": "auth-one",
}

if __name__ == "__main__":
    for i in range(3):
        openai_res = ask_with_openai(ROUTE_NAME, QUESTION, HEADERS_WITH_KEY)
        print(openai_res)
