from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):
    #5 def __init__(self, driver):
    #5     self.driver = driver

    # Python option to access mthd that doesn't need arguments w/o ()
    @property
    def url(self):
        #5 return 'http://127.0.0.1:5000/'
        return super(HomePage, self).url + '/'

    # Python option to access mthd that doesn't need arguments w/o ()
    #4 @property
    #4 def title(self):
    #4     return self.driver.find_element(*HomePageLocators.TITLE)

    # Python option to access mthd that doesn't need arguments w/o ()
    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)