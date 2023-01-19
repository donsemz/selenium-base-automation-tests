import time
from selenium.webdriver.common.keys import Keys
from page_objects.shop_page import ShopPage
from page_objects.cart_page import CartPage


class CartTest(CartPage, ShopPage):
    def setUp(self):
        super().setUp()
        print("Launching Page")
        self.open_shop_page()

    def test_add_to_cart(self):
        # add item to carts
        self.click(self.add_shoes_button)

        # assert product is added to cart
        self.assert_text("1", self.cart_count)

        # open Cart page through clicking the link
        self.click(self.go_to_cart_link)

        # get current subtotal
        total_text = self.get_text(self.price_total_text)
        print(total_text)

        # change cart quantity
        # self.send_keys(self.quantity,"2")
        self.set_value(self.quantity,"2")

        self.send_keys(self.quantity, Keys.RETURN)
        self.click(self.update_cart_button)

        # wait for load - Bad Practice
        # time.sleep(15)

        # wait for the loading to be completed
        self.wait_for_element_visible(self.loading_overlay)
        self.wait_for_element_not_visible(self.loading_overlay)

        # assert subtotal count changed
        self.wait_for_text("$300.00",self.price_total_text)
        updated_text = self.get_text(self.price_total_text)
        self.assertNotEqual(total_text,updated_text)




