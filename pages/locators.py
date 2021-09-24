from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    registration_form = (By.XPATH, "//*[@id='register_form']")
    login_form = (By.XPATH, "//*[@id='login_form']")
