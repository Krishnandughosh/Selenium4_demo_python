from selenium.webdriver.common.by import By
from webAction.webActionBase import base

class RadioButtonClick(base):
    def __init__(self):
        super().__init__()
        self.radioButtonLocator = "//*[@id=\"radio-btn-example\"]//input"
        self.radioButtonSelect = "Benz"
        self.radioBtns = []

    def clickRadioButton(self, driver):
        self.radioBtns = driver.find_elements(By.XPATH, self.radioButtonLocator)
        for btn in self.radioBtns:
            value = btn.get_attribute("value")
            if value.lower() == self.radioButtonSelect.lower():
                btn.click()
                break

    def verifyRadioButton(self):
        for btn in self.radioBtns:
            value = btn.get_attribute("value")
            if value.lower() == self.radioButtonSelect.lower():
                print(btn.is_selected())
                break

if __name__ == "__main__":
    radioBtn = RadioButtonClick()
    url=radioBtn.letsurl
    browser = input('Enter the browser: ')
    driver = radioBtn.launch_url(browser, url)
    radioBtn.clickRadioButton(driver)
    radioBtn.verifyRadioButton()
    driver.quit()
