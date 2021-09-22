from selenium.webdriver.common.by import By 

from pages.web_elements.elements import Elements
from pages.home_page import BasePage
from pages.web_elements.locators import Locator

class AmazonPage(BasePage):
  
  url = 'http://www.amazon.com'
  
  @property
  def department_dropdown(self):
    locator = Locator(by=By.CSS_SELECTOR, value='div#nav-search-dropdown-card')
    return Elements(self.browser, locator)
  
  @property
  def book_department(self):
    locator = Locator(by=By.XPATH, value="//select[@id='searchDropdownBox']")
    return Elements(self.browser, locator)
      
  @property
  def search_box(self):
    locator = Locator(by=By.XPATH, value='//*[@id="twotabsearchtextbox"]')
    return Elements(self.browser, locator)
  
  @property
  def select_item(self):
    locator = Locator(by=By.XPATH, value="(.//*[normalize-space(text()) and normalize-space(.)='Part of: Bronco and Friends (2 Books)'])[1]/preceding::span[1]")
    return Elements(self.browser, locator)
  
  @property
  def select_specific_item(self):
    locator = Locator(by=By.XPATH, value="(.//*[normalize-space(text()) and normalize-space(.)='Chris Ferrie'])[1]/preceding::span[2]")
    return Elements(self.browser, locator)
      
  @property
  def add_to_cart(self):
    locator = Locator(by=By.ID, value='add-to-cart-button')
    return Elements(self.browser, locator)
  
  @property
  def check_cart(self):
    locator = Locator(by=By.CSS_SELECTOR, value='span#nav-cart-count')
    return Elements(self.browser, locator)
  
  @property
  def check_total_sum_in_cart(self):
    locator = Locator(by=By.CLASS_NAME, value='ewc-subtotal-amount')
    return Elements(self.browser, locator)
  
  @property
  def item_price(self):
    locator = Locator(by=By.CSS_SELECTOR, value='span.a-color-price')
    return Elements(self.browser, locator)
  
  @property
  def item_page_price(self):
    locator = Locator(by=By.CSS_SELECTOR, value='span#price')
    return Elements(self.browser, locator)
  
  @property
  def go_to_cart(self):
    locator = Locator(by=By.ID, value='nav-cart-count')
    return Elements(self.browser, locator)
  
  @property
  def shopping_cart_page(self):
    locator = Locator(by=By.TAG_NAME, value='h1')
    return Elements(self.browser, locator)
  
  @property
  def items_names_in_cart_on_cart_page(self):
    locator = Locator(by=By.CSS_SELECTOR, value='span.a-truncate-cut')
    return Elements(self.browser, locator)
  
  @property
  def items_prices_in_cart_on_cart_page(self):
    locator = Locator(by=By.CSS_SELECTOR, value=('p.a-spacing-mini'))
    return Elements(self.browser, locator)
  
  @property
  def total_sum(self):
    locator = Locator(by=By.CSS_SELECTOR, value=('span#sc-subtotal-amount-activecart'))
    return Elements(self.browser, locator)
  
  @property
  def get_gift(self):
    locator = Locator(by=By.CSS_SELECTOR, value='input[type=checkbox]')
    return Elements(self.browser, locator)
  
  @property
  def change_quantity_of_first_item(self):
    locator = Locator(by=By.CSS_SELECTOR, value='select#quantity')
    return Elements(self.browser, locator)
  
  @property
  def current_quantity_of_first_item(self):
    locator = Locator(by=By.CSS_SELECTOR, value='span.a-dropdown-prompt')
    return Elements(self.browser, locator)
  
  @property
  def checkout_order(self):
    locator = Locator(by=By.CSS_SELECTOR, value='span#sc-buy-box-ptc-button')
    return Elements(self.browser, locator)
  
  @property
  def sign_in_page(self):
    locator = Locator(by=By.CSS_SELECTOR, value='h1.a-spacing-small')
    return Elements(self.browser, locator)