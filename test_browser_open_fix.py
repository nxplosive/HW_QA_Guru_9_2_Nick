import pytest
from selene import browser, be, have


@pytest.fixture()
def browser_res():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://google.com')

    yield
    browser.quit()


def test_search_google(browser_res):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_google_no_result(browser_res):
    browser.element('[name="q"]').should(be.blank).type('j0g2jg423gfed345').press_enter()
    browser.element('[style="padding-top:.33em"]').should(have.text('По запросу j0g2jg423gfed345 ничего не найдено.'))