import re
import requests
from html import unescape
from urllib.parse import urlparse
from src.utils.decorators import timing_decorator, log_io_decorator


@timing_decorator
@log_io_decorator
def cleaning_data(text: str):
    # This method is responsible for clean text
    cleanedText = unescape(text)
    cleanedText = re.sub(r"[^\w\s]", "", cleanedText)
    cleanedText = re.sub(r"<.*?>", "", cleanedText)
    cleanedText = re.sub(r"&#[0-9]+;", "", cleanedText)
    cleanedText = re.sub(r",", " ", cleanedText)
    cleanedText = re.sub(r"\s+", " ", cleanedText)
    cleanedText = cleanedText.strip()
    return cleanedText


@timing_decorator
@log_io_decorator
def get_domain_name(url: str):
    # This method is responsible for parse domain from given url
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc
    return domain_name


@timing_decorator
@log_io_decorator
def website_has_robot_txt_file(url: str):
    # This method is responsible for check robots txt file is exist
    domain = get_domain_name(url)
    if url.startswith("https://") or url.startswith("www"):
        domain = "https://" + domain
    elif url.startswith("http://"):
        domain = "http://" + domain
    else:
        return False

    robots_url = domain.rstrip('/') + '/robots.txt'
    response = requests.get(robots_url)
    if response.status_code == 200:
        return robots_url
    else:
        return False
