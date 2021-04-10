from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):  # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "login в url не найден!"

    def should_be_login_form(self):  # проверка на наличие формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login-форма не найдена!"

    def should_be_register_form(self):  # проверка на наличие формы регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register-форма не найдена!"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password_1_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)
        password_2_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)
        email_input.send_keys(email)
        password_1_input.send_keys(password)
        password_2_input.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
