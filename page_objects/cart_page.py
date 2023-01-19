from seleniumbase import BaseCase

class CartPage(BaseCase):
    price_total_text="td[class='product-subtotal']"
    quantity="input[id^='quantity']"
    update_cart_button="button[name='update_cart']"
    loading_overlay=".woocommerce-cart-form div[class*='blockOverlay']"
    cart_count="span[class='count']"

    def open_cart_page(self):
        self.open("https://practice.automationbro.com/cart/")