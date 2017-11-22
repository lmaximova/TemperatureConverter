from selenium import webdriver

class TemperatureConverterPage():
    def __init__(self, w_driver):
        self.driver = w_driver
        if self.driver.title != 'from fahrenheit to celsius - Google Search':
            raise RuntimeError("Wrong Page temp converter")


    def goToSearchPage(self):
        self.driver.find_element_by_name('q').clear()
        self.driver.find_element_by_name('q').send_keys("from fahrenheit to celsius\n")
        self.driver.implicitly_wait(5)

    def getTite(self):
        return self.driver.title

    def inputFahrenheit(self,valueOfFahrenheit):
        s = str(valueOfFahrenheit)
        self.driver.find_element_by_xpath(".//*[@id='_Aif']/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='_Aif']/input").send_keys(s)

    def actualResult(self):

        valueOfCelsius = self.driver.find_element_by_xpath(".//*[@id='_Cif']/input").get_attribute("value")
        #print(valueOfCelsius)
        return valueOfCelsius
