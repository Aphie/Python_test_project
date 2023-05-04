from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket_page(self):
        self.should_be_basket_url()
        self.should_not_be_products_in_basket()
        self.should_be_empty_basket_message()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "URL doesn't contain basket substring"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ADDED_PRODUCT), "Products are present in the basket"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Message about empty basket is not present on the page"