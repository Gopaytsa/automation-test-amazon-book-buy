from selenium import webdriver


class Browser:

  def __init__(self):
      self.driver = webdriver
      
  def chrome(self):
    options = self.driver.ChromeOptions()
    options.add_argument("--start-maximized")
    chrome = self.driver.Chrome(executable_path='./drivers/chromedriver', options=options)
    return chrome
  
  def firefox(self):
    firefox = self.driver.Firefox(executable_path='./drivers/geckodriver')
    return firefox