import time
import pytest

def test_find_basket_button(browser, language):
    print("Test received language from fixture and it is: " + str(language))
    longlink=f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.implicitly_wait(10)
    browser.get(longlink)
    buttons=browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert len(buttons) != 0, "No button 'ADD TO BASKET' on the page " + longlink
    time.sleep(15)