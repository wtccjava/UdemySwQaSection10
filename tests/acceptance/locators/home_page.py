from selenium.webdriver.common.by import By

class HomePageLocators:

    #3 TITLE = By.TAG_NAME, 'h1'  # short way of doing tuple.  same as (By.TAG_NAME, 'h1')
    NAVIGATION_LINK = By.ID, 'blog-link'
