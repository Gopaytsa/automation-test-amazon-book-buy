class BasePage:
  
  def __init__(self, browser):
    self.browser = browser
    
  def homepage(self, url, shop):
    if shop == 'amazon':
      return self.browser.get(url['amazon'])
    else:
      return self.browser.get(url['heroku'])