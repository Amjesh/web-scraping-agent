import traceback
from fastapi import HTTPException
from src.utils.decorators import timing_decorator, log_io_decorator


@timing_decorator
@log_io_decorator
def error_handler(error, status_code):
    # This function is handle error/exception
    print(isinstance(error, Exception))
    if isinstance(error, Exception):
        errorMsg = traceback.format_exc()
    elif isinstance(error, str):
        errorMsg = error
    else:
        error = "Something went wrong! Please try again."

    raise HTTPException(
        status_code=status_code, detail=errorMsg)
