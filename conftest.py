import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose language in standart format, en-gb is by default")


@pytest.fixture(scope="function")
def browser(request):   
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")   
    print("Fixture received language from options and it is: " + str(language))
    return(language)