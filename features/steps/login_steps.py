import pandas as pd
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import time


def read_excel_data(file_path):
    data = pd.read_excel(file_path)
    return data.to_dict(orient='records')


@given('the login page is opened')
def step_open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)  # Implicit wait to create realtime decto
    context.login_page = LoginPage(context.driver)
    context.login_page.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    context.data = read_excel_data("data/login_data.xlsx")


@when('I enter the credentials from row {row_number} from excel')
def step_enter_credentials_from_excel(context, row_number):
    row_number = int(row_number)
    row = context.data[row_number]
    username = row['username']
    password = row['password']
    expected_message = row['message']
    expected_url = row['expected_url']

    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    context.login_page.click_login()

    wait = WebDriverWait(context.driver, 10)
    try:
        # Implemented validation using successful url redirection
        current_url = context.driver.current_url
        time.sleep(3)

        if current_url == expected_url and current_url == ("https://opensource-demo.orangehrmlive.com/web/index.php"
                                                           "/dashboard/index"):

            actual_message = "Login successful"
        else:
            actual_message = "Invalid username or password"

        # Logging the actual URL and message for debugging
        print(f"Row {row_number} - Expected URL: {expected_url}, Actual URL: {current_url}")
        print(f"Row {row_number} - Expected Message: {expected_message}, Actual Message: {actual_message}")

        assert expected_message == actual_message, f"Expected: {expected_message}, but got: {actual_message}"
        context.login_page.take_screenshot(f"result_{username}_{password}")
    except Exception as e:
        time.sleep(2)
        context.login_page.take_screenshot("Error_Screen_shot")
        time.sleep(2)
        context.driver.quit()
        raise e


@then('I take a screenshot')
def step_take_screenshot(context):
    time.sleep(2)
    context.login_page.take_screenshot("final_screenshot")
    time.sleep(2)
    context.driver.quit()
