from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException



class Elements(object):
  def __init__(self, browser, locator):
    self.browser = browser
    self.locator = locator
    
  def find(self):
    try:
      WebDriverWait(self.browser, 20).until(
      ec.visibility_of_element_located((self.locator))
    )
    except TimeoutException:
      print('Element not found because of timeout')
    return None
  
  def get_elements_text_list(self):
    elements = WebDriverWait(self.browser, 10).until(
      ec.visibility_of_all_elements_located((self.locator))
    )
    text_list = []
    for element in elements:
      text_list.append(element.text)
    return text_list
  
  def input_text(self, txt):
    element = WebDriverWait(self.browser, 10).until(
      ec.presence_of_element_located((self.locator))
    )
    element.send_keys(txt)
    return None
  
  def checkbox(self):
    elements = WebDriverWait(self.browser, 10).until(
      ec.presence_of_all_elements_located((self.locator))
    )
    elements[1].click()
    return None
  
  def go_to_element(self, dep_name):
    element = WebDriverWait(self.browser, 10).until(
      ec.presence_of_element_located((self.locator))
    )
    Select(element).select_by_visible_text(dep_name)
    return None
  
  def click_second_button(self):
    elements = WebDriverWait(self.browser, 10).until(
      ec.presence_of_all_elements_located((self.locator))
    )
    elements[1].click()
    return None
  
  def click(self):
    element = WebDriverWait(self.browser, 10).until(
      ec.element_to_be_clickable((self.locator))
    )
    element.click()
    return None
  
  def sumbit_action(self):
    element = WebDriverWait(self.browser, 10).until(
      ec.element_to_be_clickable((self.locator))
    )
    element.submit()
    return None
  
  def current_page_url(self):
    return self.browser.current_url
  
  def is_check_box_selected(self):
    elements = WebDriverWait(self.browser, 10).until(
      ec.presence_of_all_elements_located((self.locator))
    )
    if elements[1].is_selected():
      return True
    return None
  
  def text(self):
    try:
      element = WebDriverWait(self.browser, 10).until(
        ec.visibility_of_element_located((self.locator))
      )
      text = element.text
      return text
    except TimeoutException:
      print('Element not found because of timeout')   
  
  def chenge_quantity(self, text_item):
    elements = WebDriverWait(self.browser, 10).until(
      ec.presence_of_all_elements_located((self.locator))
    )
    Select(elements[0]).select_by_visible_text(text_item)
    return None

  def check_actual_qty_first_item(self):
    elements = WebDriverWait(self.browser, 10).until(
      ec.presence_of_all_elements_located((self.locator))
    )
    return elements[0].text

  def attribute(self, attr_name):
    element = WebDriverWait(self.browser, 10).until(
      ec.visibility_of_element_located((self.locator))
    )
    attribute = element.get_attribute(attr_name)
    return attribute
