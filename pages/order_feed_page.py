import allure
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage
from stuff.pathways import Pathways
import time
from selenium.common import StaleElementReferenceException


class OrderPage(BasePage):

    @allure.step("Клик на заказ")
    def click_order(self):
        self.click_thing(OrderFeedLocators.first_order)

    @allure.step("Проверка модалки")
    def check_order_modal(self):
        return self.wait_thing(OrderFeedLocators.order_modal)

    @allure.step("Получить количество заказов за всё время")
    def get_overall_counter(self):
        return self.wait_thing(OrderFeedLocators.overall_counter).text

    @allure.step("Получить количество заказов за сегодня")
    def get_today_counter(self):
        return self.wait_thing(OrderFeedLocators.today_counter).text

    @allure.step("Получить номер заказа в работе")
    def get_in_progress_id(self):
        self.wait_thing(OrderFeedLocators.progress_status)
        return self.wait_thing(OrderFeedLocators.progress_status).text

    @allure.step("Перейти на фид")
    def go_to_feed(self):
        return self.driver.get(Pathways.ORDER_FEED)

    @allure.step("Получить номер первого заказа в фиде")
    def fetch_first_id(self):
        order_id = self.wait_thing(OrderFeedLocators.first_order_id).text
        return order_id

    def wait_for_order_in_progress(self, created_order_number, timeout=15):
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                orders_in_progress = self.get_in_progress_id()
                if created_order_number in orders_in_progress:
                    return True
            except StaleElementReferenceException:
                continue
        return False

