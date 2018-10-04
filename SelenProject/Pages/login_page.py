'''
Created on Oct 2, 2018

@author: Leher
'''
from Base.Selenium_Driver import SeleniumDriver
import Utilities.Customlogger as c1
import logging


class LoginPage(SeleniumDriver):

    log =c1.customizedLogger(logging.DEBUG)

    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)   
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.elementClick(self._login_link,locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        #self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[@id='navbar']//span[text()='User Settings']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result
  
#     def  verifyLogout(self):
#         self.isElementPresent("//img[@class='gravatar']", locatorType="xpath")
#         self.elementClick("/img[@class='gravatar']", locatorType="xpath")
#         result=self.getElement("//a[@href='/sign_out']", locatorType="xpath")
#         result.click()
#         return result
     
        
        
        
    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()
 

