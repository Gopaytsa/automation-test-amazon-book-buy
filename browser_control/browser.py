from selenium import webdriver


class Browser:

  def __init__(self):
      self.driver = webdriver
      
  def chrome(self):
    chrome = self.driver.Chrome(executable_path='./drivers/chromedriver')
    return chrome
  
  def firefox(self):
    firefox = self.driver.Firefox(executable_path='./drivers/geckodriver')
    return firefox