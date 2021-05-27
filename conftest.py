import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_Language = None
    user_Language = request.config.getoption("language")

    if (user_Language is not None):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_Language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("you have to choose a language")
        
    
    yield browser
    browser.quit()
