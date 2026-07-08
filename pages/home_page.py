import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    LOGIN_LINK = (By.CLASS_NAME, "ico-login")
    SEARCH_BOX = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.search-box-button")
    REGISTER_LINK = (By.CLASS_NAME, "ico-register")

    @allure.step("Go to register page")
    def go_to_register(self):
        self.click(self.REGISTER_LINK)

    @allure.step("Go to login page")
    def go_to_login(self):
        self.click(self.LOGIN_LINK)

    @allure.step("Search for product: {product}")
    def search_product(self, product):
        self.type(self.SEARCH_BOX, product)
        self.click(self.SEARCH_BUTTON)
