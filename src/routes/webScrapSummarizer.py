import validators
from fastapi import APIRouter, Depends, HTTPException, Request
from src.controllers.WebScrapSummarizerController import WebScrapSummarizerController
from src.schemas.index import SuccessResponse, WebScrapSummarizerSchema
from src.utils.error_handling import error_handler
from src.utils.auth import authenticate
from src.utils.temp_db import temp_data


router = APIRouter(
    prefix="/webscrap/summarizer",
    tags=['Web Scrap Summarizer']
)


@router.post('/', response_model=SuccessResponse)
async def web_scrap_summarizer(request: WebScrapSummarizerSchema, token: str = Depends(authenticate)):
    if not token:
        return error_handler("Invalid auth token", 500)

    if not validators.url(request.url):
        return error_handler(f"Invalid url '{request.url}'", 500)

    # save request id in temp_data
    temp_data['id'] = request.id
    return await WebScrapSummarizerController.web_scrap_summarizer(request)
