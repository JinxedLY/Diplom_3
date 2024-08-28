import allure
from stuff.helpers import OrderMake
from pages.order_feed_page import OrderPage


class TestOrderFeed:

    @allure.title("Проверка модалки с детялями заказа")
    def test_click_order_get_modal_success(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_feed()
        order_page.click_order()
        assert order_page.check_order_modal()

    @allure.title("Проверка отображения заказа пользователя в ленте")
    def test_check_for_user_order_in_feed_success(self, driver, create_user, login_user):
        order_page = OrderPage(driver)
        created_order_number = "#0" + str(OrderMake.order_create(create_user))
        order_page.go_to_feed()
        first_order = order_page.fetch_first_id()
        assert created_order_number == first_order

    @allure.title("Проверка увеличения счетчика Выполнено за всё время")
    def test_check_overall_counter_increase_success(self, driver, create_user, login_user):
        order_page = OrderPage(driver)
        order_page.go_to_feed()
        counter_before = order_page.get_overall_counter()
        OrderMake.order_create(create_user)
        order_page.refresh_page()
        counter_after = order_page.get_overall_counter()
        assert counter_after > counter_before

    @allure.title("Проверка увления счетчика Выполнено за сегодня")
    def test_check_today_counter_increase_success(self, driver, create_user, login_user):
        order_page = OrderPage(driver)
        order_page.go_to_feed()
        counter_before = int(order_page.get_today_counter())
        OrderMake.order_create(create_user)
        order_page.refresh_page()
        counter_after = int(order_page.get_today_counter())
        assert counter_after > counter_before

    @allure.title("Проверка появления заказа в разделе В работе")
    def test_check_for_order_in_progress_success(self, driver, create_user, login_user):
        order_page = OrderPage(driver)
        order_page.go_to_feed()
        order_page.refresh_page()
        OrderMake.order_create(create_user)
        created_order_number = "0" + str(OrderMake.order_create(create_user))
        found = order_page.wait_for_order_in_progress(created_order_number)
        assert found