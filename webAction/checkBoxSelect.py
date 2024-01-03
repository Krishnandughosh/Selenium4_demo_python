from selenium.webdriver.common.by import By
from webAction.webActionBase import base

class checkBoxSelecet(base):
    def __init__(self):
        super().__init__()
        self.checkBoxLocator = "//*[@id=\"checkbox-example-div\"]//input"
        self.checkBoxSelect = ["bmw", "honda"]
        self.checkBox = []

    def clickCheckBoxButton(self, driver):
        self.checkBox = driver.find_elements(By.XPATH, self.checkBoxLocator)
        for btn in self.checkBox:
            value = btn.get_attribute("value")
            if value.lower() in self.checkBoxSelect:
                btn.click()


    def verifyCheckBox(self):
        for btn in self.checkBox:
            if btn.is_selected():
                value = btn.get_attribute("value")
                print(value)
                print(btn.is_selected())


if __name__ == "__main__":
    radioBtn = checkBoxSelecet()
    url=radioBtn.letsurl
    browser = input('Enter the browser: ')
    driver = radioBtn.launch_url(browser, url)
    radioBtn.clickCheckBoxButton(driver)
    radioBtn.verifyCheckBox()
    driver.quit()
