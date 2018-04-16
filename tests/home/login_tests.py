from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTests:

    def test_valid_login(self):
        base_url = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)

        login_link = driver.find_element(By.LINK_TEXT, "Login")
        login_link.click()

        email_field = driver.find_element(By.ID, "user_email")
        email_field.send_keys("test@email.com")

        pwd_field = driver.find_element(By.ID, "user_password")
        pwd_field.send_keys("abcabc")

        login_btn = driver.find_element(By.NAME, "commit")
        login_btn.click()

        avtar_icon = driver.find_element(By.XPATH, "//div[@id='navbar']//span[text()='User Settings']")

        if avtar_icon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

        driver.quit()


test = LoginTests()
test.test_valid_login()