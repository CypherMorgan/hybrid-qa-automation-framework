import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):

    PRODUCT_LINK = (By.CSS_SELECTOR, ".product-title a")

    @allure.step("Open first product in search results")
    def open_first_product(self):
        self.click(self.PRODUCT_LINK)
