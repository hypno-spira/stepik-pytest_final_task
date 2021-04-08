from .pages.product_page import ProductPage
import time


def test_adding_to_basket_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.match_names_of_books()
    page.match_prices_of_books()
