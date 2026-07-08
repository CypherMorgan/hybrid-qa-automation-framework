import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_LINK = (By.CSS_SELECTOR, "span.cart-label")
    REMOVE_CHECKBOXES = (By.NAME, "removefromcart")
    UPDATE_CART_BUTTON = (By.NAME, "updatecart")
    TERMS_CHECKBOX = (By.ID, "termsofservice")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    @allure.step("Go to cart page")
    def go_to_cart(self):
        self.click(self.CART_LINK)

    @allure.step("Clear cart items")
    def clear_cart(self):
        items = self.driver.find_elements(*self.REMOVE_CHECKBOXES)
        if items:
            for item in items:
                item.click()
            self.click(self.UPDATE_CART_BUTTON)

    @allure.step("Proceed to checkout")
    def checkout(self):
        self.click(self.TERMS_CHECKBOX)
        self.click(self.CHECKOUT_BUTTON)
