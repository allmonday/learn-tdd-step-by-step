from selenium import webdriver
import unittest

class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_list(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('TO-DO', self.browser.title)
        self.fail('finish the test')

if __name__ == "__main__":
    unittest.main(warnings='ignore')

