from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_constructor(self):
        self.click_thing(MainPageLocators.constructor_button)

    def click_order_feed(self):
        self.click_thing(MainPageLocators.order_feed_button)

    def click_dash(self):
        self.click_thing(MainPageLocators.dash_button)

    def click_sauce(self):
        self.click_thing(MainPageLocators.ingredient_button)

    def modal_check(self):
        return self.wait_thing(MainPageLocators.ingredient_modal).is_displayed()

    def add_sauce(self):
        sauce = self.wait_thing(MainPageLocators.ingredient_button)
        target = self.wait_thing(MainPageLocators.constructor)
        self.actions.click_and_hold(sauce)
        self.actions.move_to_element(target)
        self.actions.release(target)
        self.actions.perform()

    def counter_check(self):
        return self.wait_thing(MainPageLocators.ingredient_counter).text !=0

    def make_order(self):
        self.click_thing(MainPageLocators.make_order_button)

    def check_order(self):
        return self.wait_thing(MainPageLocators.order_modal)