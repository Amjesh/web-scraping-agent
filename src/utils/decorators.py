
import time
import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a console handler and set its level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and add it to the console handler
formatter = logging.Formatter("%(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(
            f"{func.__name__} executed in {round(execution_time,3)} seconds")
        return result
    return wrapper


def log_io_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Function {func.__name__} called!")
        result = func(*args, **kwargs)
        logger.info(f'Function {func.__name__} returned "{result[0:200]}..."')
        return result
    return wrapper
