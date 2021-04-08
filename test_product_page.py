from .pages.product_page import ProductPage
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


@pytest.mark.parametrize('link_tail', linktail)
def test_guest_can_add_product_to_basket(browser, link_tail):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link_tail}"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    #time.sleep(5)
    page.match_names_of_books()
    page.match_prices_of_books()
