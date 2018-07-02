from behave import *
#1 from selenium import webdriver
#1 from selenium.webdriver.common.by import By

#2 from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')

@then('There is a title shown on the page')
def step_impl(context):
    #1 title_tag = context.browser.find_element(By.TAG_NAME, 'h1')
    #2 title_tag = context.browser.find_element(*HomePageLocators.TITLE)  #1 * deconstructs tuple
    #6 page = HomePage(context.browser) #2
    page = BasePage(context.browser) #6
    #2 assert title_tag.is_displayed()
    assert page.title.is_displayed() #2

@step('The title tag has content "(.*)"')
def step_impl(context, content):
    #1 title_tag = context.browser.find_element(By.TAG_NAME, 'h1')
    #2 title_tag = context.browser.find_element(*HomePageLocators.TITLE)
    page = BasePage(context.browser)  #6
    assert page.titletext == content #6

@then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.driver)
    assert page.posts_section.is_displayed()
    