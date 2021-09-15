from selenium import webdriver


class Browser:
  
  """
  This class allow to lunch webdriver and open test in different browsers usin spesific drivers as: chromedriver and geckodriver.
  """
  
  def __init__(self):
      self.driver = webdriver
      
  def chrome(self):
    """
    Launches Google Chrome browser by chromedriver.
    """
    chrome = self.driver.Chrome(executable_path='./drivers/chromedriver')
    return chrome
  
  def firefox(self):
    """
    Launches Mozilla Firefox browser by geckodriver.
    """
    firefox = self.driver.Firefox(executable_path='./drivers/geckodriver')
    return firefox