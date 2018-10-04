'''
Created on Oct 3, 2018

@author: Leher
'''
import pytest
from selenium import webdriver
from Pages.login_page import LoginPage



@pytest.yield_fixture()
def setUp():
    print("Running CONF before execution")
    yield
    print("Running CONF after execution")
    

@pytest.yield_fixture(scope="class")   #By default scopeis "FUNCTION"
def oneTimeSetup(request,browser):
    print("Running CONF test once before execution ")
    if browser == "Chrome":
        BaseURL = "https://letskodeit.teachable.com/"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get(BaseURL)
        print("Running on Chrome")
    else:
        print("Running on other browser")
        
    if request.cls is not None:
        request.cls.driver=driver
        
    yield 
    driver.quit()
    print("Running CONF test once after execution")
    
    
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType")
    
    
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
    
    