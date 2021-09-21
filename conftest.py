import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

#function pytest_addoption
def pytest_addoption(parser):
    #parser for language
    parser.addoption('--language', action='store', default=None,
                     help="Choose language:ru,es and so on...")

#fixture for browser
@pytest.fixture(scope="function")
def browser(request):
    #checking languages
    language = request.config.getoption("language")
    language = "en"

    #Starting Chrome
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)

    #closing browser
    yield browser
    print("\nquit browser..")
    browser.quit()