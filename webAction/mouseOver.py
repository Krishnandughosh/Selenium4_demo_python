from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webAction.webActionBase import base


class moueseHover(base):
    def __init__(self):
        super().__init__()
        self.interationTab = "//a[contains(text(),'Interaction')]"
        self.header = "Droppable"
        self.pageHeader = "(//h1)[1]"
        self.listTab = "//a[contains(text(),'Interaction')]/following-sibling::ul//li"

    def select_tab(self, driver):
        tab = driver.find_element(By.XPATH, self.interationTab)
        action = ActionChains(driver)
        action.move_to_element(tab).perform()
        listDropDown = driver.find_elements(By.XPATH, self.listTab)

        for d in listDropDown:
            text = d.text
            if text.lower() == self.header.lower():
                d.click()
                break

    def verify_header(self, driver):
        text = driver.find_element(By.XPATH,self.pageHeader).text
        if text.lower() == self.header.lower():
            print(text)


if __name__ == "__main__":
    mo = moueseHover()
    url = mo.way2automationUrl
    browser = input('Enter the browser: ')
    driver = mo.launch_url(browser, url)
    mo.select_tab(driver)
    mo.verify_header(driver)
    driver.close()
