import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class ProductPage(BasePage):

    ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to cart']")
    CART_LINK = (By.CSS_SELECTOR, "span.cart-label")
    SUCCESS_BAR = (By.CSS_SELECTOR, ".bar-notification.success")

    @allure.step("Add product to cart")
    def add_to_cart(self):

        self.click(self.ADD_TO_CART)

        try:
            WebDriverWait(self.driver, 3).until(lambda d: d.switch_to.alert)
            alert = self.driver.switch_to.alert
            alert.accept()
            self.click(self.ADD_TO_CART)
        except:
            pass

        WebDriverWait(self.driver, 5).until(
            lambda d: d.find_elements(*self.SUCCESS_BAR)
        )

    @allure.step("Navigate to cart from product page")
    def go_to_cart(self):
        self.click(self.CART_LINK)