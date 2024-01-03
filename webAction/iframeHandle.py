from selenium.webdriver.common.by import By
from webAction.webActionBase import base

class WindowHandle(base):
    coursesWb = []
    windows = []
    courses = []

    def __init__(self):
        super().__init__()
        self.openWindowButtonXpath = "//*[@id='openwindow']"
        self.coursesXpath = "//*[@id='course-list']//p"
        self.expectedCourses = [
            "Web + API Test Framework - Novice To Ninja",
            "A Complete Guide",
            "Learn all Test Automation courses in one place",
            "Novice To Ninja - Build an automation framework from scratch",
            "Industry Standard Framework",
            "Framework Implementation From Scratch - Novice To Ninja"
        ]


    def get_course_names(self, driver):
        driver.switch_to.frame('courses-iframe')
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
    wh.get_course_names(driver)
    wh.verify_courses()
    driver.quit()
