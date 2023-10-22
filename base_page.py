import pytest
import time
from selenium.webdriver.common.by import By
from locators import MainPageLocators, RegistrationPageLocators, LoginPageLocators, BuyingPageLocators

class TestShop:
    @pytest.mark.usefixtures("setup_teardown")
    class TestRegistration:
        def test_registration(self, browser):
            entrance_button = browser.find_element(*MainPageLocators.ENTRANCE_BUTTON)
            entrance_button.click()
            reg_button = browser.find_element(*RegistrationPageLocators.REG_BUTTON)
            reg_button.click()
            name = browser.find_element(*RegistrationPageLocators.NAME_INPUT)
            name.send_keys("c43q45556453S34536")
            email = browser.find_element(*RegistrationPageLocators.EMAIL)
            email.send_keys("wwqcgfhkdS465456aGdffhkg@gmail.com")
            password = browser.find_element(*RegistrationPageLocators.PASSWORD)
            password.send_keys("1YK5C8ml.1")
            sec_password = browser.find_element(*RegistrationPageLocators.SEC_PASSWORD)
            sec_password.send_keys("1YK5C8ml.1")
            captcha = browser.find_element(*RegistrationPageLocators.CAPTCHA)
            captcha.click()
            button = browser.find_element(*RegistrationPageLocators.BUTTON)
            button.click()
            sec_name = browser.find_element(*RegistrationPageLocators.SEC_NAME)
            sec_name.send_keys("ghjkgjk")
            third_name = browser.find_element(*RegistrationPageLocators.THIRD_NAME)
            third_name.send_keys("ghjkgjk")
            phone_number = browser.find_element(*RegistrationPageLocators.PHONE_NUMBER)
            phone_number.send_keys("тут.нет.валидации.по.номеру")
            save_information_button = browser.find_element(*RegistrationPageLocators.SAVE_INFORMATION_BUTTON)
            save_information_button.click()
            time.sleep(1)
            welcome_text_elt = self.browser.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[1]")
            welcome_text = welcome_text_elt.text
            assert "Готово!" == welcome_text


        def test_login(self, browser):
            entrance_button = browser.find_element(*MainPageLocators.ENTRANCE_BUTTON)
            entrance_button.click()
            email = browser.find_element(*LoginPageLocators.EMAIL)
            email.send_keys("wwqcgfhkdS465456aGdffhkg@gmail.com")
            password = browser.find_element(*LoginPageLocators.PASSWORD)
            password.send_keys("1YK5C8ml.1")
            login_button = browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
            login_button.click()
            time.sleep(1)
            welcome_text_elt = self.browser.find_element(By.XPATH, "/html/body/div[7]/div[2]/div[1]")
            welcome_text = welcome_text_elt.text
            assert "Готово!" == welcome_text


    @pytest.mark.usefixtures("setup_teardown")
    class TestBuying:
        def test_buy(self, browser):
            fishing_section = browser.find_element(*BuyingPageLocators.FISHING_SECTION)
            fishing_section.click()
            spinning = browser.find_element(*BuyingPageLocators.SPINNING)
            spinning.click()
            buy = browser.find_element(*BuyingPageLocators.BUY)
            buy.click()
            basket = browser.find_element(*BuyingPageLocators.BASKET)
            basket.click()
            placing_an_order = browser.find_element(*BuyingPageLocators.PLACING_AN_ORDER)
            placing_an_order.click()
            name = browser.find_element(*BuyingPageLocators.NAME)
            name.send_keys("123")
            surname = browser.find_element(*BuyingPageLocators.SURNAME)
            surname.send_keys("123")
            patronymic = browser.find_element(*BuyingPageLocators.PATRONYMIC)
            patronymic.send_keys("123")
            mail = browser.find_element(*BuyingPageLocators.MAIL)
            mail.send_keys("123")
            telephone_number = browser.find_element(*BuyingPageLocators.TELEPHONE_NUMBER)
            telephone_number.send_keys("123")
            address = browser.find_element(*BuyingPageLocators.ADDRESS)
            address.send_keys("123")
            checkout = browser.find_element(*BuyingPageLocators.CHECKOUT)
            checkout.click()
