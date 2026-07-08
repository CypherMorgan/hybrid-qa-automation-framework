import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    BILLING_CONTINUE = (By.CSS_SELECTOR, "input.button-1.new-address-next-step-button")
    SHIPPING_CONTINUE = (By.CSS_SELECTOR, "input.button-1.shipping-method-next-step-button")
    PAYMENT_METHOD_CONTINUE = (By.CSS_SELECTOR, "input.button-1.payment-method-next-step-button")
    PAYMENT_INFO_CONTINUE = (By.CSS_SELECTOR, "input.button-1.payment-info-next-step-button")
    CONFIRM_ORDER = (By.CSS_SELECTOR, "input.button-1.confirm-order-next-step-button")

    @allure.step("Continue with billing address")
    def continue_billing(self):
        self.click(self.BILLING_CONTINUE)

    @allure.step("Continue with shipping method")
    def continue_shipping(self):
        self.click(self.SHIPPING_CONTINUE)

    @allure.step("Continue with payment method")
    def continue_payment_method(self):
        self.click(self.PAYMENT_METHOD_CONTINUE)

    @allure.step("Continue with payment info")
    def continue_payment_info(self):
        self.click(self.PAYMENT_INFO_CONTINUE)

    @allure.step("Confirm order")
    def confirm_order(self):
        self.click(self.CONFIRM_ORDER)
