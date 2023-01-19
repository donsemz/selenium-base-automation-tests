from seleniumbase import BaseCase

class ShopPage(BaseCase):
    add_shoes_button='a[aria-label="Add “Branded Converse” to your cart"]'
    go_to_cart_link="a[class='added_to_cart wc-forward']"
    search_input="#woocommerce-product-search-field-0"
    search_button="button[value='Search']"
    product_img=".woocommerce-producct-gallery__image"
    no_product_txt=".woocommerce-info"
    
    def open_shop_page(self):
        self.open("https://practice.automationbro.com/shop/")