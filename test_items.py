import time
from selenium.webdriver.common.by import By

def test_add_to_basket_button_should_be_displayed(browser):
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_basket_button.is_displayed()
    print("Button displayed")
    time.sleep(7)