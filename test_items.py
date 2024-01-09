from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_should_be_displayed(browser):
    browser.get(link)
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_basket_button.is_displayed(), "Error: Button not found"
    print("Button displayed")
    time.sleep(5)