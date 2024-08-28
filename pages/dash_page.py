import allure
from pages.base_page import BasePage
from locators.dashboard_page_locators import DashPageLocators

class DashPage(BasePage):

    @allure.step("Проверка нахождения в ЛК")
    def check_dash(self):
        return self.wait_thing(DashPageLocators.profile_button)

    @allure.step("Кликнуть Историю Заказов")
    def click_order_history(self):
        self.click_thing(DashPageLocators.order_history_button)

    @allure.step("Выйти из ЛК")
    def click_logout(self):
        self.click_thing(DashPageLocators.logout_button)

    @allure.step("Подожди прогрузки ЛК")
    def wait_for_dash(self):
        self.wait_thing(DashPageLocators.logout_button)

