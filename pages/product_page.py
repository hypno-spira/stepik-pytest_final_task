from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):  # метод для добавления в корзину
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def match_names_of_books(self):  # название товара совпадает с добавленным
        name_of_book = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        name_of_book_after_adding = self.browser.find_element(*ProductPageLocators.BOOK_NAME_AFTER)
        assert name_of_book.text == name_of_book_after_adding.text, "Названия товаров не совпадают!"

    def match_prices_of_books(self):  # стоимость корзины совпадает с ценой товара
        price_of_book = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        price_of_book_after_adding = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_AFTER)
        assert price_of_book.text == price_of_book_after_adding.text, "Стоимости товаров не совпадают!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успешном добавлении не должно появляться!"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успешном добавлении должно появляться!"
