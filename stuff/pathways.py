class Pathways:
    BASE_PATH = "https://stellarburgers.nomoreparties.site"
    BASE_API = BASE_PATH + "/api"
    USER_CREATE = BASE_API + "/auth/register"
    ORDER_CREATE = BASE_API + "/orders"
    USER_MULTIPURPOSE = BASE_API + "/auth/user"
    LOGIN_PATH = BASE_PATH + "/login"
    FORGOT_PASSWORD = BASE_PATH + '/forgot-password'
    RESET_PASSWORD = BASE_PATH + '/reset-password'
    ACCOUNT_PROFILE = BASE_PATH + '/account/profile'
    ORDER_HISTORY = BASE_PATH + '/account/order-history'
    ORDER_FEED = BASE_PATH + '/feed'