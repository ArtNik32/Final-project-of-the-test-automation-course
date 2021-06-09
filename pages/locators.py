from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_PAGE_ENTER_FORM = (By.CLASS_NAME, 'col-sm-6.login_form')
    LOGIN_PAGE_REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
