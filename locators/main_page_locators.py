from selenium.webdriver.common.by import By

class MainPageLocators:
    constructor_button = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")
    order_feed_button = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")
    dash_button = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")
    ingredient_button = (By.XPATH, ".//img[@alt = 'Соус Spicy-X']")
    ingredient_counter = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")
    ingredient_modal = (By.XPATH, "//h2[text()= 'Детали ингредиента']")
    constructor = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
    make_order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    order_modal = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")