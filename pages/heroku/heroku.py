from selenium.webdriver.common.by import By 

from pages.web_elements.elements import Elements
from pages.home_page import BasePage
from pages.web_elements.locators import Locator


class Heroku(BasePage):
  
  url = 'http://the-internet.herokuapp.com/'
  
  @property
  def dropdown(self):
    locator = Locator(by=By.CSS_SELECTOR, value="a[href='/dropdown']")
    return Elements(self.browser, locator)
  
  @property
  def challenging_dom(self):
    locator = Locator(by=By.CSS_SELECTOR, value="a[href='/challenging_dom']")
    return Elements(self.browser, locator)
  
  @property
  def dropdown_list(self):
    locator = Locator(by=By.CSS_SELECTOR, value="select#dropdown")
    return Elements(self.browser, locator)
  
  @property
  def second_option(self):
    locator = Locator(by=By.CSS_SELECTOR, value="option[value='2']")
    return Elements(self.browser, locator)
  
  @property
  def button_qux(self):
    locator = Locator(by=By.XPATH, value="//a[contains(text(), 'qux')]")
    return Elements(self.browser, locator)
  
  @property
  def button_foo(self):
    locator = Locator(by=By.XPATH, value="//a[contains(text(), 'foo')]")
    return Elements(self.browser, locator)
  
  @property
  def buttons(self):
    locator = Locator(by=By.CSS_SELECTOR, value="a.button")
    return Elements(self.browser, locator)
  
  @property
  def find_table(self):
    locator = Locator(by=By.TAG_NAME, value="table")
    return Elements(self.browser, locator)
  
  @property
  def find_table_cell(self):
    locator = Locator(by=By.XPATH, value="//td[contains(text(), 'Definiebas1')]")
    return Elements(self.browser, locator)
  
  @property
  def find_cell_in_row(self):
    locator = Locator(by=By.CSS_SELECTOR, value="a[href='#delete']")
    return Elements(self.browser, locator)