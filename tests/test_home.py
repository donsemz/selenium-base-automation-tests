from page_objects.home_page import HomePage

class HomeTest(HomePage):
    def setUp(self):
        # Call the parent BaseCase class setup method
        super().setUp()
        print("Running Before Test")

        # LOGIN
        self.login()

        # open home page
        self.open_page()

    def tearDown(self):
        print("Running After Each Test")

        # Logout
        self.open("https://practice.automationbro.com/my-account")
        self.click(".woocommerce-MyAccount-content a[href*=logout]")
        self.assert_element_visible("button[name=login]")

        # Call the parent BaseCase class tearDown method
        super().tearDown()

    def test_home_page(self):

        # assert page title
        self.assert_title("Practice E-Commerce Site – Automation Bro")

        # assert logo presence
        self.assert_element(HomePage.logo_icon)

        # click get started button and assert the url
        self.click(HomePage.get_started_btn)
        # page_url = self.get_current_url()
        # self.assert_equal(page_url,"https://practice.automationbro.com/#get-started")
        # self.assert_true("get-started" in page_url)
        self.assert_url_contains("#get-started")

        # get the text of the header and assert the value
        self.assert_text("Think different. Make different.", HomePage.heading_text)

        # Scroll to the bottom and assert copyright text
        self.scroll_to_bottom()
        print(self.get_text(HomePage.copyright_text))
        self.assert_text("Copyright © 2020 Automation Bro", HomePage.copyright_text)

    def test_navbar(self):

        expected_text_links = ['Home', 'About', 'Shop', 'Blog', 'Contact', 'My account']

        # find menu navbar
        navbar = self.find_elements(HomePage.menu_links)
        # self.find_elements("li[id*=menu-item]")

        # loop through navbar elements and assert them
        for idx, item in enumerate(navbar):
            if navbar.index(item) < 6:
                print(idx, item.text)
                self.assertEqual(expected_text_links[idx], item.text)

