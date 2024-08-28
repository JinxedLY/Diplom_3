import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from stuff.helpers import RealHumans
import requests
from stuff.pathways import Pathways
from stuff.test_data import Ingredients

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def create_user():
    payload = RealHumans.create_real_human()
    response = requests.post(Pathways.USER_CREATE, json=payload)
    yield payload, response
    token = response.json()['accessToken']
    header = {'Authorization': token}
    requests.delete(Pathways.USER_MULTIPURPOSE, headers=header)

@pytest.fixture
def login_user(driver, create_user):
    user_data = create_user[0]
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    main_page.go_to_site()
    main_page.click_dash()
    login_page.user_auth(user_data['email'], user_data['password'])

@pytest.fixture
def order_create(request, driver, create_user):
    def create_order():
        token = create_user[1].json()['accessToken']
        header = {
            "Authorization": token
        }
        payload = {
            "ingredients": [
                Ingredients.BUN,
                Ingredients.MEAT,
                Ingredients.SAUCE
            ]
        }
        response = requests.post(Pathways.ORDER_CREATE, headers=header, json=payload)
        return response.json()['order']['number']
    if request.node.get_closest_marker("auto_order"):
        return create_order()
    return create_order