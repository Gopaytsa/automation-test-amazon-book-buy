from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 


class Elements(object):
  def __init__(self, browser, locator):
    self.browser = browser
    self.locator = locator
    self.web_element = None 
    
  def find(self):
    element = WebDriverWait(self.browser, 10).until(
      ec.visibility_of_element_located((self.locator))
    )
    self.web_element = element
    return None
  
  def find_all(self):
    element = WebDriverWait(self.browser, 10).until(
      ec.visibility_of_elements_located(locator=self.locator)
    )
    self.web_element = element
    return None
  
  def input_text(self, txt):
    self.web_element.send_keys(txt)
    return None
  
  def click(self):
    element = WebDriverWait(self.browser, 10).until(
      ec.element_to_be_clickable(locator=self.locator)
    )
    element.click()
    return None
  
  def attribute(self, attr_name):
    attribute = self.web_element.get_attribute(attr_name)
    return attribute
  
  @property
  def text(self):
    text = self.web_element.text
    return text