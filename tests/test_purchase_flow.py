from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from config.config_reader import ConfigReader
from utils.data_generator import product_search_term


def test_purchase_flow(driver):

    home = HomePage(driver)

    home.go_to_login()

    login = LoginPage(driver)
    login.login(
        ConfigReader.get_username(),
        ConfigReader.get_password()
    )

    cart = CartPage(driver)
    cart.go_to_cart()
    cart.clear_cart()

    home = HomePage(driver)
    term = product_search_term()
    home.search_product(term)

    search = SearchPage(driver)
    search.open_first_product()

    product = ProductPage(driver)
    product.add_to_cart()
    product.go_to_cart()

    cart = CartPage(driver)
    cart.checkout()

    assert "Checkout" in driver.title