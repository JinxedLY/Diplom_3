import allure
from locators.login_page_locators import LoginPageLocators
from stuff.pathways import Pathways
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestPassRecovery:
    @allure.title("Проверка перехода на страницу забытого пароля при нажатии на кнопку восстановления")
    def test_redirect_to_forgotten_pass_page_success(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.go_to_site()
        main_page.click_dash()
        login_page.click_to_recovery()
        assert driver.current_url == Pathways.FORGOT_PASSWORD

    @allure.title("Проверка перехода на страницу восстановления пароля при прохождении страницу забытого пароля")
    def test_redirect_to_recovery_pass_page_success(self, driver, create_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.go_to_site()
        main_page.click_dash()
        login_page.click_to_recovery()
        email = create_user[0]['email']
        login_page.pass_email(email)
        login_page.click_recovery()
        login_page.wait_thing(LoginPageLocators.code_from_email_input_field)
        assert driver.current_url == Pathways.RESET_PASSWORD

    @allure.title("Проверка подсветки поля при нажатии на кнопку показа пароля")
    def test_password_field_highlight_success(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.go_to_site()
        main_page.click_dash()
        login_page.click_eyeball()
        assert login_page.check_field_active()

