from selenium.webdriver.common.by import By

class MainPageLocators:
    ENTRANCE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div[2]/a[3]")

class RegistrationPageLocators:
    NAME_INPUT = (By.CSS_SELECTOR, "body > main > div.container > form > div.row.flb-cc > div > div:nth-child(1) > input")
    REG_BUTTON = (By.XPATH, "/html/body/main/div[2]/form/div[2]/div/a")
    NAME = (By.CSS_SELECTOR, "body > main > div.container > form > div.row.flb-cc > div > div:nth-child(1) > input")
    EMAIL = (By.CSS_SELECTOR, "body > main > div.container > form > div.row.flb-cc > div > div:nth-child(2) > input")
    PASSWORD = (By.XPATH, "/html/body/main/div[2]/form/div[2]/div/div[3]/input")
    SEC_PASSWORD = (By.CSS_SELECTOR, "body > main > div.container > form > div.row.flb-cc > div > div:nth-child(4) > input")
    CAPTCHA = (By.XPATH, "/html/body/main/div[2]/form/div[2]/div/label/span[1]")
    BUTTON = (By.XPATH, "/html/body/main/div[2]/form/div[2]/div/button")
    SEC_NAME = (By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div/div[1]/div/div/form/div[3]/div/input")
    THIRD_NAME = (By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div/div[1]/div/div/form/div[4]/div/input")
    PHONE_NUMBER = (By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div/div[1]/div/div/form/div[6]/div/input")
    SAVE_INFORMATION_BUTTON = (By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div/div[1]/div/div/form/div[7]/button")


class LoginPageLocators:
    EMAIL = (By.CSS_SELECTOR, "body > main > div.container > form > div.row.flb-cc > div > div:nth-child(1) > input")
    PASSWORD = (By.CSS_SELECTOR, "body > main > div.container > form > div.row.flb-cc > div > div:nth-child(2) > input")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "body > main > div.container > form > div.row.flb-cc > div > button")
    SAVE_INF_BUTTON = (By.XPATH, "/html/body/main/div[2]/div[2]/div[2]/div/div[1]/div/div/form/div[7]/button")


class BuyingPageLocators:
    FISHING_SECTION = (By.XPATH, "/html/body/div[3]/div/aside/div/nav/div[5]/a")
    SPINNING = (By.XPATH, "//*[@id='products-container']/div[1]/div/div[3]/button")
    BUY = (By.XPATH, "//*[@id='products-container']/div[11]/div/div[3]/button")
    BASKET = (By.XPATH, "//*[@id='cart-header']")
    PLACING_AN_ORDER = (By.XPATH, "//*[@id='cart-page']/div[2]/aside/a[1]")
    NAME = (By.XPATH, "/html/body/main/div[2]/form/div/div/div[2]/div/input")
    SURNAME = (By.XPATH, "/html/body/main/div[2]/form/div/div/div[3]/div/input")
    PATRONYMIC = (By.XPATH, "/html/body/main/div[2]/form/div/div/div[4]/div/input")
    MAIL = (By.XPATH, "/html/body/main/div[2]/form/div/div/div[6]/div/input")
    TELEPHONE_NUMBER = (By.XPATH, "/html/body/main/div[2]/form/div/div/div[7]/div/input")
    ADDRESS = (By.XPATH, "/html/body/main/div[2]/form/div/div/div[11]/div/input")
    PAYMENT_METHOD = (By.XPATH, "/html/body/main/div[2]/form/div/div/div[10]/div/div/div[1]")
    CASH_PAYMENT = (By.XPATH,"/html/body/main/div[2]/form/div/div/div[10]/div/div/div[2]/div[2]")
    CHECKOUT = (By.XPATH, "/html/body/main/div[2]/form/aside/button")
