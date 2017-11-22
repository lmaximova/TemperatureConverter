import unittest
from src.main.Google import Google
from selenium import webdriver

class TestTemperatureConverte(unittest.TestCase):
    def setUp(self):
        #self.googlePage = Google(webdriver.Chrome("C:\\Selenium\\Chrome\\chromedriver_win32\chromedriver.exe"))
        self.googlePage = Google(webdriver.Chrome())
    def tearDown(self):
        self.googlePage.close()

    def test_tempConverterTo37(self):
        tempConverterPage = self.googlePage.goToSearchPage()
        tempConverterPage.inputFahrenheit('98.6')
        actualRes = tempConverterPage.actualResult()
        assert actualRes == '37', "Error: 98.6F is not equal 37C"

    def test_tempConverterTo0(self):
        tempConverterPage = self.googlePage.goToSearchPage()
        tempConverterPage.inputFahrenheit('32')
        actualRes = tempConverterPage.actualResult()
        assert actualRes == '0', "Error: 32F is not equal 0C"

if __name__ == '__main__':
    unittest.main()
