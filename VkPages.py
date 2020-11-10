from BaseApp import BasePage
from selenium.webdriver.common.by import By


class VkLocators:
    LOCATOR_VK_LOGIN_FIELD = (By.ID, "index_email")
    LOCATOR_VK_PASSWORD_FIELD = (By.ID, "index_pass")
    LOCATOR_VK_ENTER_BUTTON = (By.ID, "index_login_button")
    LOCATOR_VK_ACCOUNT_NAME = (By.CLASS_NAME, "top_profile_name")
    # LOCATOR_VK_TOP_PROFILE_BUTTON = (By.ID, "top_profile_menu")
    LOCATOR_VK_EXIT_BUTTON = (By.ID, "top_logout_link")
    LOCATOR_VK_TOP_PROFILE_BUTTON = (By.CLASS_NAME, "top_profile_arrow")


class LoginHelper(BasePage):

    def enter_login(self, login):
        login_field = self.find_element(VkLocators.LOCATOR_VK_LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(login)
        return login_field

    def enter_password(self, password):
        password_field = self.find_element(VkLocators.LOCATOR_VK_PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(password)
        return password_field

    def click_on_enter_button(self):
        return self.find_element(VkLocators.LOCATOR_VK_ENTER_BUTTON, time=2).click()


class ExitHelper(BasePage):

    def click_on_exit(self):
        return {self.find_element(VkLocators.LOCATOR_VK_TOP_PROFILE_BUTTON, time=2).click(),
                self.find_element(VkLocators.LOCATOR_VK_EXIT_BUTTON, time=2).click()}


class Finder(BasePage):

    def find_name(self):
        return self.find_element(VkLocators.LOCATOR_VK_ACCOUNT_NAME, time=4)
