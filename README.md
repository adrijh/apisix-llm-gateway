# LLM Gateway with Apache APISIX

This project showcases how to build a **production-grade Gateway for Large Language Models (LLMs)** using [Apache APISIX](https://apisix.apache.org/). 
It enables secure, scalable, and observable access to LLM providers like OpenAI and others.

> ✨ Learn more in the [Medium article →](https://your-medium-article-link)

---

## 🚀 Why an LLM Gateway?

LLMs in production require much more than just a simple API call. A Gateway enables:

- ⚖️ Load balancing across multiple model providers
- 🛡️ Prompt validation and guards
- 🔐 Authentication and rate-limiting
- 🔍 Observability of prompts and responses
- 🔄 Traffic shaping and routing
- 🧱 Pluggable policies per team or use case


---

## 🛠️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/adrijh/apisix-llm-gateway.git
cd apisix-llm-gateway
```

2. **Introduce your API Key** in .env file

3. **Deploy gateway**
```bash
docker compose up -d
```

You can test routes and functionalities using the `scripts/` folder
