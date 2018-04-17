from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    login_link = "Login"
    user_email = "user_email"
    user_pwd = "user_password"
    login_btn = "commit"

    def click_login_link(self):
        self.elementClick(self.login_link, locatorType="link")

    def input_email(self, email):
        self.sendKeys(email, self.user_email)

    def input_pwd(self, password):
        self.sendKeys(password, self.user_pwd)

    def click_login_btn(self):
        self.elementClick(self.login_btn, locatorType="name")

    def login_method(self, email, pwd):
        self.click_login_link()
        self.input_email(email)
        self.input_pwd(pwd)
        self.click_login_btn()

    def verify_login_success(self):
        result = self.isElementPresent("//*[@id='navbar']//span[text()='User Settings']",
                                       locatorType="xpath")
        return result

    def verify_login_failure(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def clear_field(self):
        email_field = self.getElement(locator=self.user_email)
        email_field.clear()
        pwd_field = self.getElement(locator=self.user_pwd)
        pwd_field.clear()

    def verify_title(self):
        print(self.get_title())
        if "Let's Kode It" in self.get_title():
            return True
        else:
            return False
