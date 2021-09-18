from selenium.webdriver.common.by import By 

from pages.web_elements.elements import Elements
from pages.home_page import BasePage
from pages.web_elements.locators import Locator

class AmazonPage(BasePage):
  
  @property
  def department_dropdown(self):
    locator = Locator(by=By.CSS_SELECTOR, value='#searchDropdownBox')
    return Elements(self.driver, locator)
  
  @property
  def book_department(self):
    locator = Locator(by=By.CSS_SELECTOR, value='option:nth-child(6)')
    return Elements(self.driver, locator)
  
  @property
  def submit_searc_button(self):
    locator = Locator(by=By.XPATH, value='//li/a')
    for i in locator:
      if i.text == "Children's Books":
        pass
  
  @property
  def select_item(self):
    pass