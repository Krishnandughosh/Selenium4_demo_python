from selenium.webdriver.common.by import By
from webAction.webActionBase import base

class WindowHandle(base):
    coursesWb = []
    windows = []
    courses = []

    def __init__(self):
        super().__init__()
        self.openWindowButtonXpath = "//*[@id='opentab']"
        self.coursesXpath = "//*[@id='course-list']//p"
        self.expectedCourses = [
            "Web + API Test Framework - Novice To Ninja",
            "A Complete Guide",
            "Learn all Test Automation courses in one place",
            "Novice To Ninja - Build an automation framework from scratch",
            "Industry Standard Framework",
            "Framework Implementation From Scratch - Novice To Ninja"
        ]

    def click_open_window_button(self, driver):
        btn = driver.find_element(By.XPATH, self.openWindowButtonXpath)
        btn.click()

    def get_course_names(self, driver):
        self.windows = driver.window_handles
        for w in self.windows:
            driver.switch_to.window(w)
            self.coursesWb = driver.find_elements(By.XPATH, self.coursesXpath)
            for c in self.coursesWb:
                self.courses.append(c.text)

    def verify_courses(self):
        for c in self.courses:
            print(c + ' :: ' + str(c in self.expectedCourses))

if __name__ == "__main__":
    wh = WindowHandle()
    url = wh.letsurl
    browser = input('Enter the browser: ')
    driver = wh.launch_url(browser, url)
    wh.click_open_window_button(driver)
    wh.get_course_names(driver)
    wh.verify_courses()
    driver.quit()
