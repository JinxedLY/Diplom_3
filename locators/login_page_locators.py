from selenium.webdriver.common.by import By

class LoginPageLocators:
    email_field = (By.XPATH, ".//input[@name = 'name']")
    password_field = (By.XPATH, ".//input[@name = 'Пароль']")
    auth_button = (By.XPATH, "//button[text() = 'Войти']")
    to_recovery_button = (By.XPATH, "//a[text() = 'Восстановить пароль']")
    recovery_button = (By.XPATH, "//button[text() = 'Восстановить']")
    code_from_email_input_field = (By.XPATH, ".//label[text() = 'Введите код из письма']")
    show_password_button = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")
    field_active = (By.CSS_SELECTOR, ".input.input_status_active")