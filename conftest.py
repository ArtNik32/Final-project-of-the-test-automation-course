import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    #выбор языка браузера в консоли
    parser.addoption('--language',
    action = 'store',
    default = None,
    help = 'Choose language = ru, en, es, ..')
    #выбор браузера в консоли
    parser.addoption('--browser_name',
    action = 'store',
    default = 'chrome',
    help = 'Choose browser = chrome or firefox')

@pytest.fixture(scope = 'function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser_language = request.config.getoption('language')
    #проверка выбора браузера и языка
    if browser_name == 'chrome' and browser_language != None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        print('\nstar chrome browser for test..')
        browser = webdriver.Chrome(options=options)
    #проверка выбора браузера и языка
    elif browser_name == 'firefox' and browser_language != None:
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", browser_language)
        print('\nstar firefox browser for test..')
        browser = webdriver.Firefox(firefox_profile=fp)
    #если язык не выбран - вывод сообщния об ошибке
    else:
        raise pytest.UsageError('--language should be ru, en, es, ..')

    yield browser
    print('\nquit browser..')
    browser.quit()
