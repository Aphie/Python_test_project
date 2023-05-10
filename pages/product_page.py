from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def click_on_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()

    def click_on_basket_button_without_quiz(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_notification_about_product(self):
        self.should_be_notification_about_added_product()
        self.should_be_product_name_on_the_page()
        self.should_be_product_name_in_message_equal_to_product_name()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button is not present"

    def should_be_notification_about_added_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_NOTIFICATION), "Message about added product is not present"

    def should_be_product_name_on_the_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not present"

    def should_be_product_name_in_message_equal_to_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_NOTIFICATION).text in self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, "Was added wrong product to basket"

    def should_be_notification_about_price(self):
        self.shoud_be_notification_for_price()
        self.should_be_product_price_on_page()
        self.should_be_equal_price_for_product_and_price_in_message()

    def shoud_be_notification_for_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not present"

    def should_be_product_price_on_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_NOTIFICATION), "Product price in notification is not present"

    def should_be_equal_price_for_product_and_price_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_NOTIFICATION).text in self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text, "Price in basket not equal to price of product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not dissappear, but should"
