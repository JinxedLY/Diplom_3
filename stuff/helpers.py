from faker import Faker
from stuff.test_data import Ingredients
import requests
from stuff.pathways import Pathways

class RealHumans:
    @staticmethod
    def create_real_human():
        fake = Faker()
        email = fake.email()
        password = fake.password()
        name = fake.first_name()
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload

class OrderMake:
    @staticmethod
    def order_create(create_user):
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