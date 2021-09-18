from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 

from browser_control.browser import Browser


class Elements(Browser):
  def __init__(self, value, by):
    self.driver = Browser().deriver
    self.value = value
    self.by = by
    self.locator = (self.by, self.value)
    self.web_element = None 
    self.find()
    
  def find(self):
    element = WebDriverWait(self.driver, 10).until(
      ec.visibility_of_element_located(locator=self.locator)
    )
    self.web_element = element
    return None
  
  def input_text(self, txt):
    self.web_element.send_keys(txt)
    return None
  
  def click(self):
    element = WebDriverWait(self.driver, 10).until(
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