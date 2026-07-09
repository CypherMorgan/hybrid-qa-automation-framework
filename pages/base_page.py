import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from config.config_reader import ConfigReader


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, ConfigReader.get_explicit_wait())

    @allure.step("Click element")
    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except StaleElementReferenceException:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()

    @allure.step("Type text: {text}")
    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Get element text")
    def get_text(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    @allure.step("Check element visibility")
    def is_visible(self, locator):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except:
            return False

    @allure.step("Open page: {path}")
    def open(self, path=""):
        base_url = ConfigReader.get_base_url()
        self.driver.get(f"{base_url}{path}")
