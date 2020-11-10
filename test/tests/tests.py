import allure
from VkPages import LoginHelper
from VkPages import ExitHelper
from VkPages import Finder
from VkPages import VkLocators


class TestLoginExit:

    def test_login(self, browser, user_login, user_password):
        vk_page = LoginHelper(browser)
        vk_page.go_to_site()
        vk_page.enter_login(user_login)
        vk_page.enter_password(user_password)
        vk_page.click_on_enter_button()
        vk_finder = Finder(browser)
        user_name = vk_finder.find_name()
        assert user_name.text == "Мирон"

    def test_exit(self, browser):
        vk_page = ExitHelper(browser)
        vk_page.click_on_exit()
        assert vk_page.find_element(VkLocators.LOCATOR_VK_ENTER_BUTTON)
