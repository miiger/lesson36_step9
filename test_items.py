from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = f" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basketBtn_with_language(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    button = None
    try:   
        button = browser.find_element_by_class_name("btn-add-to-basket")
    finally:
        assert button is not None, 'Could not find a basket button'
    

    
    
    

    

    
