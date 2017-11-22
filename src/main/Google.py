from selenium import webdriver
from src.main.TemperatureConverterPage import TemperatureConverterPage

class Google():

    def __init__(self, w_driver):
        self.driver = w_driver
        self.driver.get("http://google.com")
        self.driver.implicitly_wait(5)
        if self.driver.title != "Google":
            raise RuntimeError("Wrong Google Page")

    def goToSearchPage(self):
        self.driver.find_element_by_name('q').clear()
        self.driver.find_element_by_name('q').send_keys("from fahrenheit to celsius\n")
        self.driver.implicitly_wait(5)
        numRest = self.driver.find_element_by_id('resultStats').text
        return TemperatureConverterPage(self.driver)

    def getTite(self):
        return self.driver.title

    def close(self):
        self.driver.close()
