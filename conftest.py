from pytest import fixture
from json import load as json_load
from browser_control.browser import Browser

def pytest_addoption(parser):
  parser.addoption(
    '--browser',
    action='store',
    default='chrome',
    help='Browser for tests run'
  )
    
  
@fixture(scope='function')
def driver(request):
    driver = request.config.getoption("--browser")
    if 'firefox' in driver:
      driver = Browser().firefox()
    else:
      driver = Browser().chrome()
    
      yield driver
      driver.quit()
