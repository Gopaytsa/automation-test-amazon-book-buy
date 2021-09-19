from selenium.webdriver.common.by import By 
import icecream as ic

from pages.web_elements.elements import Elements
from pages.home_page import BasePage
from pages.web_elements.locators import Locator


class Heroku(BasePage):
  
  @property
  def home_page_examples_list(self):
    locator = Locator(by=By.CSS_SELECTOR, value='div#content li')
    return Elements(self.driver, locator)
  
  @property
  def dropdown_list(self):
    locator = Locator(by=By.ID, value='dropdown')
    return Elements(self.driver, locator)
  
  @property
  def options_in_dropdown_list(self):
    locator = Locator(by=By.TAG_NAME, value='option')
    return Elements(self.driver, locator)
  
  @property
  def buttons(self):
    locator = Locator(by=By.CSS_SELECTOR, value='a.button')
    return Elements(self.driver, locator)
  
  @property
  def find_table_cals(self):
    locator = Locator(by=By.CSS_SELECTOR, value='div.large-10 tr td')
    return Elements(self.driver, locator)