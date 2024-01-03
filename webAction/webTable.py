from selenium.webdriver.common.by import By

from webAction.webActionBase import base


class webTable(base):
    def __init__(self):
        super().__init__()
        self.webTableXpath = "//table[@id='product']//tr//td[@class='course-name']"
        self.authorNameXpath = "(//table[@id='product']//td[@class='author-name'])["
        self.priceXpath = "(//table[@id='product']//td[@class='price'])["
        self.searchCourseName = "Python Programming Language"
        self.expectedAuthoName = "Let's Kode It"
        self.expectedPrice = "30"
        self.counter = 1

    def check_web_table(self, driver):
        table = driver.find_elements(By.XPATH, self.webTableXpath)
        for td in table:
            courseName = td.text
            if courseName.lower() == self.searchCourseName.lower():
                break
            self.counter = self.counter + 1
        self.authorNameXpath = self.authorNameXpath + str(self.counter) + ']'
        self.priceXpath = self.priceXpath + str(self.counter) + ']'
        authorName = driver.find_element(By.XPATH, self.authorNameXpath).text
        price = driver.find_element(By.XPATH, self.priceXpath).text
        if authorName.lower() == self.expectedAuthoName.lower():
            print(authorName)
        if price.lower() == self.expectedPrice.lower():
            print(price)



if __name__ == "__main__":
    webtable = webTable()
    url = webtable.letsurl
    browser = input('Enter the browser: ')
    driver = webtable.launch_url(browser, url)
    webtable.check_web_table(driver)
    driver.close()
