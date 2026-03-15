import pytest
from pytest_bdd import scenarios, given, when, then
from pagefile.loginpage import LoginPage
from utility.logger import get_logger

logger = get_logger()           # create logger instance
# Link feature file

scenarios('../features/login.feature')

@given('user launch browser')
def launch_browser(driver):
    logger.info("user launching browser")
    driver.get("https://www.saucedemo.com")
    return driver  # can return driver if needed


@when('user enter username and password')
def enter_credentials(driver):
    logger.info("user enter username and password")
    loginpage = LoginPage(driver)
    loginpage.enter_username("standard_user")
    loginpage.enter_password("secret_sauce")

@when('user click on login button')
def click_login(driver):
    logger.info("user click on login utton")
    loginpage = LoginPage(driver)
    loginpage.click_login()


@then('user should see the Dashboard page')
def verify_dashboard(driver):
    logger.info("user can see Dashboard")
    if "inventory" not in driver.current_url:
        driver.save_screenshot("dashboard_error.png")
    assert "inventory" in driver.current_url
