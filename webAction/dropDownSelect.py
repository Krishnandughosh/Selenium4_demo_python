from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webAction.webActionBase import base


class SelectDropDown(base):
    def __init__(self):
        super().__init__()
        self.dropDownLocator = "//*[@id='carselect']"   
        self.dropDownSelect = "Benz"

    def select_dropDown(self, driver):
        dropDown = driver.find_element(By.XPATH, self.dropDownLocator)
        self.select = Select(dropDown)
        self.select.select_by_value(self.dropDownSelect.lower())

    def verify_dropDown(self):
        selected = self.select.first_selected_option.text
        print(selected)


if __name__ == "__main__":
    radioBtn = SelectDropDown()
    url = radioBtn.letsurl
    browser = input('Enter the browser: ')
    driver = radioBtn.launch_url(browser, url)
    radioBtn.select_dropDown(driver)
    radioBtn.verify_dropDown()
    driver.quit()
