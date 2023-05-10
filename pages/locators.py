from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    ADDED_PRODUCT = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRODUCT_NAME_IN_NOTIFICATION = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRODUCT_PRICE_IN_NOTIFICATION = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
