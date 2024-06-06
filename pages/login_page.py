from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # wait time added to create a realtime user experience
        self.username_input = (By.XPATH, "//input[@placeholder='Username']")
        self.password_input = (By.XPATH, "//input[@placeholder='Password']")
        self.login_button = (By.XPATH, "//button[normalize-space()='Login']")

    def open(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        username_element = self.wait.until(EC.presence_of_element_located(self.username_input))
        username_element.clear()
        username_element.send_keys(username)

    def enter_password(self, password):
        password_element = self.wait.until(EC.presence_of_element_located(self.password_input))
        password_element.clear()
        password_element.send_keys(password)

    def click_login(self):
        login_button_element = self.wait.until(EC.element_to_be_clickable(self.login_button))
        login_button_element.click()

    def take_screenshot(self, name):
        self.driver.save_screenshot(f"screenshots/{name}.png")
