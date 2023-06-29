import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from src.utils.decorators import timing_decorator, log_io_decorator
from src.utils.prompts import web_scrap_briefing_prompt


@log_io_decorator
@timing_decorator
def summarize_with_simple_method(content):
    key = os.environ.get('OPENAI_API_KEY')
    llm = OpenAI(openai_api_key=key, temperature=0)
    prompt = web_scrap_briefing_prompt()
    chain = LLMChain(llm=llm, prompt=prompt)
    finalResult = chain.run(content)
    return finalResult
