
import ssl
import requests
from typing import Any
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from src.utils.helper import website_has_robot_txt_file, cleaning_data
from src.utils.decorators import timing_decorator, log_io_decorator
from src.utils.webhook import call_webhook_with_error


# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context


@timing_decorator
@log_io_decorator
def scrap_text(url: str):
    try:
        robotFileUrl = website_has_robot_txt_file(url)
        if not robotFileUrl:
            return call_webhook_with_error("Url has not a robots.txt file", 500)

        robot_parser = RobotFileParser()
        robot_parser.set_url(robotFileUrl)
        robot_parser.read()

        allowed = robot_parser.can_fetch("*", url)
        if not allowed:
            return call_webhook_with_error("Given url is not allow to scrap",  500)

        # Fetch web text
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.prettify())

        # print(soup.find('title').text)

        paragraphs = []
        # Replace with the appropriate HTML tags
        all_paragraphs = soup.find_all("p")
        for paragraph in all_paragraphs:
            paragraphs.append(cleaning_data(paragraph.text))

        rawContent = soup.get_text()
        rawData = ' '.join(paragraphs)

        content = cleaning_data(rawData)
        return content
    except Exception as e:
        return call_webhook_with_error(e, 500)
