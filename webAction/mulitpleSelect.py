from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webAction.webActionBase import base


class SelectDropDown(base):
    def __init__(self):
        super().__init__()
        self.dropDownLocator =  "//*[@id=\"multiple-select-example\"]"
        self.dropDownSelect = ["Apple", "Orange"]

    def select_dropDown(self, driver):
        dropDown = driver.find_element(By.XPATH, self.dropDownLocator)
        self.select = Select(dropDown)
        for d in self.dropDownSelect:
            self.select.select_by_value(d.lower())

    def verify_dropDown(self):
        selected = self.select.all_selected_options
        for s in selected:
            print(s.text)


if __name__ == "__main__":
    radioBtn = SelectDropDown()
    url = radioBtn.letsurl
    browser = input('Enter the browser: ')
    driver = radioBtn.launch_url(browser, url)
    radioBtn.select_dropDown(driver)
    radioBtn.verify_dropDown()
    driver.quit()
