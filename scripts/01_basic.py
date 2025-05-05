from common import ask_with_requests, ask_with_openai

ROUTE_NAME = "basic"
QUESTION = "What is 1 + 1?"
HEADERS = {"Content-Type": "application/json"}

if __name__ == "__main__":
    requests_res = ask_with_requests(ROUTE_NAME, QUESTION, HEADERS)
    print(requests_res)

    openai_res = ask_with_openai(ROUTE_NAME, QUESTION, HEADERS)
    print(openai_res)
