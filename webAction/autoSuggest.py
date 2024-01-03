from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from webAction.webActionBase import base


class autoSuggest(base):
    def __init__(self):
        super().__init__()
        self.textBoxLocator = "//*[@id=\"autosuggest\"]"
        self.initialText = "App"
        self.autoFillOptionXpath = "//*[@class=\"ui-menu-item\"]"
        self.selectString = "Native App"
        self.autoFillOptionListXpath = "//*[@class='ui-menu-item']/a"

    def select_Text(self, driver):
        textBox = driver.find_element(By.XPATH, self.textBoxLocator)
        textBox.send_keys(self.initialText)
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.autoFillOptionXpath)))
        options = element.find_elements(By.XPATH, self.autoFillOptionListXpath)


        for o in options:
            if o.text.lower() == self.selectString.lower():
                o.click()


if __name__ == "__main__":
    autoSug = autoSuggest()
    url = autoSug.letsurl
    browser = input('Enter the browser: ')
    driver = autoSug.launch_url(browser, url)
    autoSug.select_Text(driver)
    # driver.quit()
