import ssl
# from typing import Any
import json
from src.schemas.index import WebScrapSummarizerSchema
from src.utils.scraper import scrap_text
from src.utils.webhook import call_webhook_with_success, call_webhook_with_error
from src.models.simple_method import summarize_with_simple_method


class WebScrapSummarizerController:

    def __init__(self):
        self.test = "test data"

    @classmethod
    async def web_scrap_summarizer(self, payload: WebScrapSummarizerSchema):
        url = payload.url

        try:
            # Get web scrap text
            content = scrap_text(url)

            # Create brief using Open AI
            summarizedContent = summarize_with_simple_method(content)

            # Call spritz TS API
            call_webhook_with_success({
                "status": 'completed',
                "data": {
                    "title": "",
                    "summarizedContent": summarizedContent,
                    "originalContent": content
                }
            })

            return {"data": "", "detail": content}
        except Exception as e:
            return call_webhook_with_error(e, 500)
