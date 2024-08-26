from faker import Faker

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

class Ingredients:
    BUN = '61c0c5a71d1f82001bdaaa6d'
    MEAT = '61c0c5a71d1f82001bdaaa6f'
    SAUCE = '61c0c5a71d1f82001bdaaa72'