from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webAction.webActionBase import base


class alertHandle(base):
    def __init__(self):
        super().__init__()
        self.iframeXpath = "(//iframe[@class='demo-frame'])[1]"
        self.simpleAlertTabXpath = "//a[contains(text(),'Simple Alert')]"
        self.simpleAlertButtonXpath = "//button[contains(text(),'Click the button to display an alert box:')]"
        self.inputAlertTabXpath = "//a[contains(text(),'Input Alert')]"
        self.inputAlertButtonXpath = "//button[contains(text(),'Click the button to demonstrate the Input box.')]"
        self.alertMessage = "I am an alert box!"
        self.inputName = "Rahul Shetty"
        self.displayMessge = "Hello " + self.inputName + "! How are you today?"
        self.displayMessageXpath = "//p[@id='demo']"
        self.frames = []

    def clickTab(self, driver, tabPath):
        tab = driver.find_element(By.XPATH, tabPath)
        tab.click()

    def explicitWait(self, xpath):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def simple_alert(self, driver):
        self.frames = driver.find_elements(By.TAG_NAME, 'iframe')
        driver.switch_to.frame(self.frames[0])
        driver.find_element(By.XPATH, self.simpleAlertButtonXpath).click()
        alert = driver.switch_to.alert
        msg = alert.text
        alert.accept()
        driver.switch_to.default_content()
        print(msg)

    def input_alert(self, driver):
        driver.switch_to.frame(self.frames[1])
        self.explicitWait(self.inputAlertButtonXpath)
        element=driver.find_element(By.XPATH, self.inputAlertButtonXpath)
        element.click()
        alert = driver.switch_to.alert
        alert.dismiss()
        element.click()
        alert.send_keys(self.inputName)
        alert.accept()
        msg = driver.find_element(By.XPATH, self.displayMessageXpath).text
        if msg == self.displayMessge:
            print(msg)


if __name__ == "__main__":
    al = alertHandle()
    url = al.way2automationUrl
    browser = input('Enter the browser: ')
    driver = al.launch_url(browser, url)
    al.clickTab(driver, al.simpleAlertTabXpath)
    al.simple_alert(driver)
    al.clickTab(driver, al.inputAlertTabXpath)
    al.input_alert(driver)
