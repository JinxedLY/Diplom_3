from selenium.webdriver.common.by import By

class DashPageLocators:
    profile_button = (By.XPATH, ".//a[text() = 'Профиль']")
    order_history_button = (By.XPATH, ".//a[text() = 'История заказов']")
    logout_button = (By.XPATH, ".//button[text() = 'Выход']")