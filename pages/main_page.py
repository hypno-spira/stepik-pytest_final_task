from .base_page import BasePage
from selenium.webdriver.common.by import By
from .login_page import LoginPage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class MainPage(BasePage):
    # Заглушка
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
