from selenium import webdriver


class RunSelenium:
    def runningSelenium(self, url, browser):
        if browser.lower() == "chrome":
            driver = webdriver.Chrome()
            print(browser + ':: running in Chrome')
        elif browser.lower() == "firefox":
            driver = webdriver.Firefox()
            print(browser + ':: running in Firefox')
        elif browser.lower() == "edge":
            driver = webdriver.Edge()
            print(browser + ':: running in Edge')
        else:
            driver = webdriver.Chrome()
            print(browser + ':: running in Default')

        return driver


if __name__ == "__main__":
    r = RunSelenium()
    url = "https://google.com"
    browser = input("Enter the browser::\n")
    driver = r.runningSelenium(url, browser)
    driver.maximize_window()
    driver.get(url)

    print(driver.title)
    driver.close()
