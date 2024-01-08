import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.get(link)

    if language == "es" or "fr" or "ar" or "ca" or "cs": # перечислить все необходимые/поддерживаемые языки
        print(f"\nTest started with chosen language - {language}")
        language_selector = browser.find_element(By.CSS_SELECTOR, f"[value='{language}']")
        language_selector.click()
        submit_language_button = browser.find_element(By.CSS_SELECTOR, "#language_selector .btn-default")
        submit_language_button.click()
    else:
        raise pytest.UsageError("--language incorrect")
    yield browser
    print("\nquit browser..")
    browser.quit()