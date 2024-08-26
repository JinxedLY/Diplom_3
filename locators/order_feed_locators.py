from selenium.webdriver.common.by import By

class OrderFeedLocators:
    first_order = (By.XPATH, '(//a[contains(@class, "OrderHistory_")])[1]')
    first_order_name = (By.XPATH, '(//h2[contains(@class, "text text_type_main-medium mb-2")])[1]')
    first_order_id = (By.XPATH, '(//p[contains(@class, "text text_type_digits-default")])[1]')
    overall_counter = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[1]')
    today_counter = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[2]')
    progress_status = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]//li[contains(@class, "text")][1]')
    order_modal = (By.XPATH, '//div[contains(@class, " Modal_modal__contentBox__")]')