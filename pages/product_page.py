from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        # метод для добавления в корзину
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def match_names_of_books(self):
        # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили
        name_of_book = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        name_of_book_after_adding = self.browser.find_element(*ProductPageLocators.BOOK_NAME_AFTER)
        assert name_of_book.text == name_of_book_after_adding.text, "Названия книг не совпадают!"

    def match_prices_of_books(self):
        # Стоимость корзины совпадает с ценой товара
        price_of_book = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        price_of_book_after_adding = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_AFTER)
        assert price_of_book.text == price_of_book_after_adding.text, "Стоимость книг не совпадают!"

