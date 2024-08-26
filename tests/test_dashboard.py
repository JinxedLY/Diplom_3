import allure

from pages.main_page import MainPage
from pages.dash_page import DashPage
from stuff.pathways import Pathways


class TestDashboard:

    @allure.title("Проверка перехода в личный кабинет")
    def test_redirect_to_dashboard_success(self, driver, create_user, login_user):
        main_page = MainPage(driver)
        dash_page = DashPage(driver)
        main_page.click_dash()
        dash_page.wait_for_dash()
        assert driver.current_url == Pathways.ACCOUNT_PROFILE

    @allure.title("Проверка перехода в историю заказов")
    def test_redirect_to_order_history_success(self, driver, create_user, login_user):
        main_page = MainPage(driver)
        dash_page = DashPage(driver)
        main_page.click_dash()
        dash_page.click_order_history()
        assert driver.current_url == Pathways.ORDER_HISTORY

    @allure.title("Проверка выхода из аккаунта")
    def test_logout_success(self, driver, create_user, login_user):
        main_page = MainPage(driver)
        dash_page = DashPage(driver)
        main_page.click_dash()
        dash_page.click_logout()
        dash_page.wait_for_logout()
        assert driver.current_url == Pathways.LOGIN_PATH
