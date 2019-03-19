from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import os

class BasePage(object):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__ + "/.."))
    ENTIRE_ROOT = ROOT_DIR + '/' + ("chromedriver")
    driver = webdriver.Chrome(executable_path=ENTIRE_ROOT)
    driver.get('https://ts-yyz-r1.tribalscale.lan/index.php')
    wait = WebDriverWait(driver, 5)

    def type(self, locator, value):
        self.wait.until(expected_conditions.presence_of_element_located(locator)).send_keys(value)

    def click(self, locator):
        self.wait.until(expected_conditions.presence_of_element_located(locator)).click()

    def quit_driver(self):
        self.driver.quit()


class LoginPage(BasePage):
    username = (By.ID, 'usernamefld')
    password = (By.ID, 'passwordfld')
    login_button = (By.NAME, 'login')
    USERNAME = os.environ.get("VPN_USERNAME")
    PASSWORD = os.environ.get("VPN_PASSWORD")

    def log_in(self):
        self.type(self.username, self.USERNAME)
        self.type(self.password, self.PASSWORD)
        self.click(self.login_button)


class HomePage(BasePage):
    vpn_button = (By.XPATH, '//ul[@class = "nav navbar-nav"]/li[5]')
    ipsec_button = (By.XPATH, '//a[@href = "/vpn_ipsec.php"]')
    enable_disable_button = (By.NAME, 'toggle_0')
    apply_change_button = (By.NAME, 'apply')

    def open_vpn_setting(self):
        self.click(self.vpn_button)
        self.click(self.ipsec_button)

    def reset_vpn(self):
        button = BasePage.wait.until(expected_conditions.presence_of_element_located(self.enable_disable_button))

        if button.text in ['Disable']:
            self.click(self.enable_disable_button)
            self.click(self.apply_change_button)
            self.click(self.enable_disable_button)
            self.click(self.apply_change_button)
        else:
            self.click(self.enable_disable_button)
            self.click(self.apply_change_button)


class MainTest():
    login_page = LoginPage()
    home_page = HomePage()
    try:
        login_page.log_in()
        home_page.open_vpn_setting()
        home_page.reset_vpn()
    finally:
        BasePage.driver.quit()