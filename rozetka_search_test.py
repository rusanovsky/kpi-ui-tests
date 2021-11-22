from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Test(TestCase):
    def test_rozetka_search(self):
        search_request = 'pampers'
        url = 'https://rozetka.com.ua/ua/'

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.implicitly_wait(10)

        browser.get(url)

        browser.find_element_by_css_selector('[name="search"]').send_keys(search_request)
        browser.find_element_by_css_selector('[name="search"]').send_keys(Keys.ENTER)

        actualResult = browser.current_url

        expectedResult = search_request

        assert expectedResult in actualResult

        browser.close()
