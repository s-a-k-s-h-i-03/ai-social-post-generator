# AI Social Media Post Generator

A FastAPI-based AI backend that generates Instagram-style captions for small businesses using prompt engineering and LangChain Runnable pipelines.

## Features
- FastAPI REST API
- LangChain Runnable chains
- Prompt templates for marketing content
- Swagger UI for testing
- Graceful fallback when LLM quota is exceeded

## Tech Stack
- Python
- FastAPI
- LangChain
- OpenAI API
- Pydantic

## API Endpoint
**POST** `/generate-post`

### Sample Input
```json
{
  "shop_type": "Café",
  "occasion": "Weekend",
  "offer": "10% off"
}

### Sample Output
```json
{
  "caption": "☕ Weekends are better with coffee! Enjoy 10% off today.",
  "hashtags": ["#smallbusiness", "#localshop"],
  "cta": "Visit us today!"
}



---

### 🔹 Run Locally (CORRECT)

```markdown
## Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload


---

### 🔹 Swagger UI link (CORRECT)

```markdown
Open Swagger UI:
http://127.0.0.1:8000/docs

