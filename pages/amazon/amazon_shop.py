from selenium.webdriver.common.by import By 

from pages.web_elements.elements import Elements
from pages.home_page import BasePage
from pages.web_elements.locators import Locator

class AmazonPage(BasePage):
  
  url = 'http://www.amazon.com'
  
  @property
  def department_dropdown(self):
    locator = Locator(by=By.CSS_SELECTOR, value='#searchDropdownBox')
    return Elements(self.browser, locator)
  
  @property
  def book_department(self):
    locator = Locator(by=By.XPATH, value='//li/a')
    return Elements(self.browser, locator)
      
  @property
  def search_box(self):
    locator = Locator(by=By.ID, value='twotabsearchtextbox')
    return Elements(self.browser, locator)
  
  @property
  def submit_searc_button(self):
    locator = Locator(by=By.ID, value='nav-search-submit-button')
    return Elements(self.browser, locator)
  
  @property
  def select_item(self):
    locator = Locator(by=By.XPATH, value='//h2/a/span')
    return Elements(self.browser, locator)
      
  @property
  def add_to_cart(self):
    locator = Locator(by=By.ID, value='add-to-cart-button')
    return Elements(self.drivebrowserr, locator)
  
  @property
  def check_cart(self):
    locator = Locator(by=By.ID, value='nav-cart-count')
    return Elements(self.browser, locator)
  
  @property
  def check_total_sum_in_cart(self):
    locator = Locator(by=By.CLASS_NAME, value='ewc-subtotal-amount')
    return Elements(self.browser, locator)
  
  @property
  def item_price(self):
    locator = Locator(by=By.CLASS_NAME, value='a-offscreen'[0])
    return Elements(self.browser, locator)
  
  @property
  def go_to_cart(self):
    locator = Locator(by=By.ID, value='nav-cart-count')
    return Elements(self.browser, locator)
  
  @property
  def shopping_cart_page(self):
    locator = Locator(by=By.CSS_SELECTOR, value='div#sc-active-cart h1')
    return Elements(self.browser, locator)
  
  @property
  def cart_page_subtotal(self):
    locator = Locator(by=By.ID, value='sc-subtotal-label-activecart')
    return Elements(self.browser, locator)
  
  @property
  def cart_page_total_sum(self):
    locator = Locator(by=By.CSS_SELECTOR, value='span#sc-subtotal-amount-activecart')
    return Elements(self.browser, locator)
  
  @property
  def item_name_in_cart_on_cart_page(self):
    locator = Locator(by=By.CSS_SELECTOR, value='span.a-truncate-full')
    return Elements(self.browser, locator)
  
  @property
  def item_price_in_cart_on_cart_page(self):
    locator = Locator(by=By.CSS_SELECTOR, value=('p.a-spacing-mini'))
    return Elements(self.browser, locator)
  
  @property
  def first_item_is_a_gift(self):
    locator = Locator(by=By.CSS_SELECTOR, value='input[type=checkbox]')
    return Elements(self.browser, locator[1])
  
  @property
  def change_quantity_of_first_item(self):
    locator = Locator(by=By.CSS_SELECTOR, value='span.sc-action-quantity')
    return Elements(self.browser, locator)
  
  @property
  def select_three_items(self):
    locator = Locator(by=By.CSS_SELECTOR, value='#a-popover-4 li:nth-child(4)')
    return Elements(self.browser, locator)
  
  @property
  def checkout_order(self):
    locator = Locator(by=By.CSS_SELECTOR, value='span#sc-buy-box-ptc-button')
    return Elements(self.browser, locator)
  
  @property
  def sign_in_page(self):
    locator = Locator(by=By.CSS_SELECTOR, value='h1.a-spacing-small')
    return Elements(self.browser, locator)