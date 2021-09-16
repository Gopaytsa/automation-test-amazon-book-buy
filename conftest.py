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
def browser(website):
  if website == 'heroku':
    driver = Browser().firefox()
  else:
    driver = Browser().chrome()
  
  yield driver
  driver.quit()


@fixture(scope='session')
def app_config(url):
  with open(f'config.json', 'r') as config_file:
    config = json_load(config_file)
  config['url'] = url
  config_file.close()
  return config