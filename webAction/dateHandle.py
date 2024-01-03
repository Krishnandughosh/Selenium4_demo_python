from datetime import datetime

from selenium.webdriver.common.by import By

from webAction.webActionBase import base


class dateHandle(base):

    def __init__(self):
        super().__init__()
        self.pastDate = "18/1/2022"
        self.futureDate = "8/1/2025"
        self.today = "31/12/2023"
        self.prevXpath = "//span[contains(text(),'Prev')]"
        self.nextXpath = "//span[contains(text(),'Next')]"
        self.dateXpath = "//input[@id='datepicker']"
        self.currentDate, self.currentMonth, self.currentYear = 0, 0, 0
        self.targetDate, self.targetMonth, self.targetYear = 0, 0, 0
        self.calMonth, self.calYear = 0, 12
        self.dateSelectXpath = ''
        self.calMonth, self.calYear = 0, 12
        self.frames = []

    def calculated_Dates(self, inputDate):
        self.currentDate = int(datetime.today().date().day)
        self.currentMonth = int(datetime.today().date().month)
        self.currentYear = int(datetime.today().date().year)
        self.targetDate = int(inputDate.split('/')[0])
        self.targetMonth = int(inputDate.split('/')[1])
        self.targetYear = int(inputDate.split('/')[2])
        if self.currentYear > self.targetYear:
            self.calYear = (self.currentYear - self.targetYear) * self.calYear
        else:
            self.calYear = (self.targetYear - self.currentYear) * self.calYear
        if self.currentMonth > self.targetMonth:
            self.calMonth = self.currentMonth - self.targetMonth
        else:
            self.calMonth = self.targetMonth - self.currentMonth
        print(self.calYear)
        print(self.calMonth)

    def select_Calander(self, driver):
        self.frames = driver.find_elements(By.TAG_NAME, 'iframe')
        driver.switch_to.frame(self.frames[0])
        driver.find_element(By.XPATH, self.dateXpath).click()
        if self.currentYear > self.targetYear:
            for i in range(self.calYear):
                driver.find_element(By.XPATH, self.prevXpath).click()
        else:
            for i in range(self.calYear):
                driver.find_element(By.XPATH, self.nextXpath).click()
        if self.currentMonth > self.targetMonth:
            for i in range(self.calYear):
                driver.find_element(By.XPATH, self.prevXpath).click()
        else:
            for i in range(self.calYear):
                driver.find_element(By.XPATH, self.nextXpath).click()
        self.dateSelectXpath = "//a[contains(text()," + str(self.targetDate) + ")]"
        driver.find_element(By.XPATH, self.dateSelectXpath).click()


if __name__ == "__main__":
    dtHndl = dateHandle()
    url = dtHndl.way2automationDateUrl
    browser = input('Enter the browser: ')
    driver = dtHndl.launch_url(browser, url)
    dtHndl.calculated_Dates(dtHndl.pastDate)
    dtHndl.select_Calander(driver)
    driver.refresh()
    print('------------')
    dtHndl.calculated_Dates(dtHndl.futureDate)
    dtHndl.select_Calander(driver)
    driver.refresh()
    print('------------')
    dtHndl.calculated_Dates(dtHndl.today)
    dtHndl.select_Calander(driver)
    driver.quit()
