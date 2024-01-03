from selenium.webdriver.common.by import By

from webAction.webActionBase import base


class uploadFileHandle(base):
    def __init__(self):
        super().__init__()
        self.registrationTab = "//a[contains(text(),'Registration')]"
        self.uploadFile = "//label[contains(text(),'Your Profile Picture')]/following-sibling::input"
        self.filePath = "C:\\Users\\krish\\Pictures\\IMG_0171.jpg"

    def upload_File_Function(self, driver):
        driver.find_element(By.XPATH, self.registrationTab).click()
        upLdBtn = driver.find_element(By.XPATH, self.uploadFile)
        upLdBtn.send_keys(self.filePath)
        driver.get_screenshot_as_file("..//screenshot/Registrationscreenshotsup.png")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.get_screenshot_as_file("..//screenshot/Registrationscreenshotsbotton.png")


if __name__ == "__main__":
    uFHndle = uploadFileHandle()
    url = uFHndle.way2automationUrl
    browser = input('Enter the browser: ')
    driver = uFHndle.launch_url(browser, url)
    uFHndle.upload_File_Function(driver)
    driver.close()
