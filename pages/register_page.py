from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):

    GENDER_MALE = (By.ID, "gender-male")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")

    SUCCESS_MESSAGE = (By.CLASS_NAME, "result")

    def register_user(self, first, last, email, password):

        self.click(self.GENDER_MALE)
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.type(self.CONFIRM_PASSWORD, password)

        self.click(self.REGISTER_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
