from pages.base import WebPage
from pages.elements import WebElement
import os


class AuthPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://petfriends1.herokuapp.com/login'

        super().__init__(web_driver, url)

    email = WebElement(id="email")

    password = WebElement(id="pass")

    btn_success = WebElement(xpath='//button[@type="submit"]')







