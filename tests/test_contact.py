from seleniumbase import BaseCase

class ContactTest(BaseCase):
    def test_contact_page(self):
        # open home page
        self.open("https://practice.automationbro.com")

        # go to contact page and check the url is correct
        self.click("#menu-item-493 > a")
        self.assert_url_contains("contact")

        # screenshot before filling the fields - scroll to form
        self.scroll_to("#evf-form-277")
        self.save_screenshot("empty-contact-form","custom_screenshots")

        # fill in the fields
        self.send_keys("#evf-277-field_ys0GeZISRs-1", "bobby")
        self.send_keys("#evf-277-field_LbH5NxasXM-2", "bobby@hitme.com")
        self.send_keys("#evf-277-field_66FR384cge-3", "7865438907")
        self.send_keys("#evf-277-field_yhGx3FOwr2-4", "I want some help")

        # screenshot filled form
        self.scroll_to("#evf-form-277")
        self.save_screenshot("filled-contact-form", "custom_screenshots")

        # click submit button
        self.click("#evf-submit-277")

        # check page navigation success message
        self.assert_text("Thanks for contacting us! We will be in touch with you shortly",
                         "#primary > div > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-e2bbe43.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div > div > div > section.elementor-section.elementor-inner-section.elementor-element.elementor-element-c58f8f7.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div.elementor-column.elementor-col-33.elementor-inner-column.elementor-element.elementor-element-7648d39 > div > div > div > div > div > div > div")