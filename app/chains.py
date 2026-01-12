from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from app.prompt_templates import BASE_PROMPT

# Initialize LLM
llm = OpenAI(temperature=0.7)

# Prompt template
prompt = PromptTemplate(
    input_variables=["shop_type", "occasion", "offer"],
    template=BASE_PROMPT,
)

# Runnable chain 
post_chain = prompt | llm
