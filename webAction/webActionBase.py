from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver


class base:

    def __init__(self):
        self.letsurl = "https://www.letskodeit.com/practice"
        self.way2automationUrl="https://www.way2automation.com/way2auto_jquery/alert.php#load_box"
        self.way2automationDateUrl="https://www.way2automation.com/way2auto_jquery/datepicker.php#load_box"
    def launch_url(self, browser, url):
        if (browser.lower() == "chrome"):
            self.driver = ChromeWebDriver()
            print(browser + ':: running in Chrome')
        elif browser.lower() == "firefox":
            self.driver = FirefoxWebDriver()
            print(browser + ':: running in Firefox')
        elif browser.lower() == "edge":
            self.driver = EdgeWebDriver()
            print(browser + ':: running in Edge')
        else:
            self.driver = ChromeWebDriver()
            print(browser + ':: running in Default')
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        print(self.driver.title)

        return self.driver
