from pages.home_page import HomePage
from pages.register_page import RegisterPage
from utils.data_generator import user_profile


def test_register(driver):

    home = HomePage(driver)
    home.go_to_register()

    register = RegisterPage(driver)

    user = user_profile()

    register.register_user(
        user["first_name"],
        user["last_name"],
        user["email"],
        user["password"]
    )

    assert "completed" in register.get_success_message().lower()
