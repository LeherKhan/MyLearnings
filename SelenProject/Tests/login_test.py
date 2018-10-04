
from Pages.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)


#     BaseURL = "https://letskodeit.teachable.com/"
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(4)     Shifted to Conftest

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com","abcabc")
        result=self.lp.verifyLoginSuccessful()
        assert result == True
        print("successful LogIN")
    
            
            
        
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test123@email.com","abcabc")
        result=self.lp.verifyLoginFailed()
        assert result == True
        print("Unsuccessful LogIN")
        self.lp.clearFields()
         
   
        
    
        
        
         
    