from seleniumbase import BaseCase

class UploadTest(BaseCase):
    def test_visible_upload(self):
        # open page
        self.open("https://the-internet.herokuapp.com/upload")

        # get file path
        file_path = "./data/23881.pdf"

        # upload file
        self.choose_file("#file-upload", file_path)

        # click upload button
        self.click("#file-submit")

        # assert uploaded text
        self.assert_text("File Uploaded!", "#content > div > h3")

    def test_hidden_upload(self):
        # open page
        self.open("https://practice.automationbro.com/cart/")

        # get file path
        file_path = "data/23881.pdf"

        # add js to remove hidden class
        remove_hidden_class = "document.getElementById('#upfile_1').classList.remove('file_input_hidden')"
        self.add_js_code(remove_hidden_class)

        # upload file
        self.choose_file("#upfile_1", file_path)

        # click upload button
        self.click("#upload_1")

        # assert uploaded text
        self.assert_text("uploaded successfully", "#wfu_messageblock_header_1_label_1")
