class BasePage:
  
  url = None
  
  def __init__(self, browser):
    self.browser = browser
    
  def homepage(self):
    return self.browser.get(self.url)