from fastapi import FastAPI, HTTPException
from app.schemas import PostRequest, PostResponse
from app.chains import post_chain
from openai import RateLimitError

app = FastAPI()

@app.post("/generate-post", response_model=PostResponse)
async def generate_post(data: PostRequest):
    try:
        result = post_chain.invoke({
            "shop_type": data.shop_type,
            "occasion": data.occasion,
            "offer": data.offer or "No offer"
        })

        text = result.content

    except Exception as e:
        # Fallback when OpenAI quota is exceeded
        text = f"🔥 {data.occasion} special at our {data.shop_type}! {data.offer or 'Visit us today'}."

    return {
        "caption": text.split("\n")[0],
        "hashtags": ["#smallbusiness", "#localshop"],
        "cta": "Visit us today!"
    }
