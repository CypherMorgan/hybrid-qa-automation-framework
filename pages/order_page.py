import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".section.order-completed .title")

    @allure.step("Get order success message")
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    @allure.step("Verify order was successful")
    def is_order_successful(self):
        return "completed" in self.get_success_message().lower()
