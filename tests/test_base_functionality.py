import allure
from conftest import driver
from pages.main_page import MainPage
from stuff.pathways import Pathways


class TestBaseFunctionality:
    @allure.title("Проверка перехода по клику на Конструктор")
    def test_open_constructor_success(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_dash()
        main_page.click_constructor()
        assert driver.current_url == Pathways.BASE_PATH + "/"

    @allure.title("Проверка перехода на Ленту заказов")
    def test_open_order_feed_success(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_order_feed()
        assert driver.current_url == Pathways.ORDER_FEED

    @allure.title("Проверка открытия модалки с деталями по индигриенту")
    def test_ingredient_modal_success(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_sauce()
        assert main_page.modal_check()

    @allure.title("Проверка увеличения счетчика при добавления индигриента")
    def test_ingredient_counter_increase_success(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.add_sauce()
        assert main_page.counter_check()

    @allure.title("Проверка возможности создания заказа из-под юзера")
    def test_order_create_with_auth_success(self, driver, create_user, login_user):
        main_page = MainPage(driver)
        main_page.add_sauce()
        main_page.make_order()
        assert main_page.check_order()
