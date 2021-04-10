from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import time
import pytest

linktail = [
    "?promo=offer0",
    "?promo=offer1",
    "?promo=offer2",
    "?promo=offer3",
    "?promo=offer4",
    "?promo=offer5",
    "?promo=offer6",
    pytest.param("?promo=offer7", marks=pytest.mark.xfail),
    "?promo=offer8",
    "?promo=offer9"
]


@pytest.mark.register
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)  # фикстура - сетап для регистрации нового пользователя
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        register_page = LoginPage(browser, link)
        register_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "meowMEoW234!meoWW"
        register_page.register_new_user(email, password)
        register_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):  # не должно быть сообщения об успешном добавлении в корзину
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):  # добавить товар в корзину (без параметризации)
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.match_names_of_books()
        page.match_prices_of_books()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):  # нет сообщения после добавления
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.need_review
# @pytest.mark.parametrize('link_tail', linktail)
def test_guest_can_add_product_to_basket(browser):  # добавить товар в корзину (БЕЗ параметризации)
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"  # {link_tail}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.match_names_of_books()
    page.match_prices_of_books()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):  # сообщение исчезает после добавления в корзину
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_success_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):  # юзер не видит товар в корзине (пр. стр)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_items_in_basket()
    basket_page.should_be_text_about_basket_is_empty()


def test_guest_should_see_login_link_on_product_page(browser):  # видимость ссылки на логин со страницы продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):  # переход на страницу логина со страницы продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
