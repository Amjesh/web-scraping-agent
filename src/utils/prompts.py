from langchain.prompts import PromptTemplate


def web_scrap_briefing_prompt():
    # Make a prompt for fetch invoice amount
    # @params {str} sentence
    # @return {str} prompt
    prompt_creation_template = (
        '"""/'
        "You are a ChatGPT model trained to summarize web news articles \n"
        "Act like Senior journalist \n"
        "Please provide a brief summary of the following article.\n {content}"
        '"""'
    )

    prompt = PromptTemplate(
        input_variables=["content"],
        template=prompt_creation_template,
    )
    return prompt
