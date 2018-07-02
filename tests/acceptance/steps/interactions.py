from behave import *
from selenium import webdriver

from tests.acceptance.page_model.base_page import BasePage

use_step_matcher('re')

@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    # link = context.driver.find_element_by_id(link_id)
    page = BasePage(context.driver)
    links = page.navigation
    # find right link
    matching_links = [l for l in links if l.text == link_text]
    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()

