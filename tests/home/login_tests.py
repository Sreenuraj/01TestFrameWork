import unittest
from pages.home.login_page import LoginPage
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.login_object = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.login_object.login_method("test@email.com", "abcabc")
        result1 = self.login_object.verify_title()
        assert result1 == True
        result2 = self.login_object.verify_login_success()
        assert result2 == True


    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.login_object.login_method("test@email.com", "abcabcabc")
        result = self.login_object.verify_login_failure()
        assert result == True

