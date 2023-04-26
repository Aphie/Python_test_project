import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',help="Choose browser language")

@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    browser = None
    s=Service('C:\\Users\\s.andreyuk\\python environments\\selenium_cource_hw\\chromedriver_win32\\chromedriver.exe')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
    browser = webdriver.Chrome(service=s, options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
