from selenium.common import NoSuchElementException

from page_objects.shop_page import ShopPage


class ShopTest(ShopPage):

    def setUp(self):
        # Call the parent BaseCase class setup method
        super().setUp()
        print("Running Before Test")

        # open shop page
        self.open_shop_page()

    def test_search_products(self):
        # search for the product
        self.send_keys(self.search_input,"Sunglasses")
        self.click(self.search_button)

        # assert the product image
        try:
            self.assert_element_present(self.product_img)
        except NoSuchElementException:
            print("product not found")
            self.assert_text("No products were found matching your selection.", self.no_products_txt)





