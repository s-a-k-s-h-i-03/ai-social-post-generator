from pydantic import BaseModel
from typing import List, Optional

class PostRequest(BaseModel):
    shop_type: str
    occasion: str
    offer: Optional[str] = None

class PostResponse(BaseModel):
    caption: str
    hashtags: List[str]
    cta: str
