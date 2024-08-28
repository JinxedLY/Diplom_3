import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):

    @allure.step("Заполнить поле Email")
    def pass_email(self, email):
        self.send_keys(LoginPageLocators.email_field, email)

    @allure.step("Заполнить поле Пароль")
    def pass_password(self, password):
        self.send_keys(LoginPageLocators.password_field, password)

    @allure.step("Нажать кнопку Войти")
    def click_auth(self):
        self.click_thing(LoginPageLocators.auth_button)

    @allure.step("Авторизовать юзера")
    def user_auth(self, email, password):
        self.pass_email(email)
        self.pass_password(password)
        self.click_auth()

    @allure.step("Кликнуть восстановление пароля")
    def click_to_recovery(self):
        self.click_thing(LoginPageLocators.to_recovery_button)

    @allure.step("Кликнуть кнопку восстановления пароля")
    def click_recovery(self):
        self.click_thing(LoginPageLocators.recovery_button)

    @allure.step("Кликнуть кнопку показа пароля")
    def click_eyeball(self):
        self.click_thing(LoginPageLocators.show_password_button)

    @allure.step("Проверка активности поля")
    def check_field_active(self):
        return self.wait_thing(LoginPageLocators.field_active)

    @allure.step("Подожди прогрузки страницы логина")
    def wait_for_logout(self):
        self.wait_thing(LoginPageLocators.auth_button)