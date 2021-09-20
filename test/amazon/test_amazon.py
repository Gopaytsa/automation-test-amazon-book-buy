from pytest import mark
from pages.amazon.amazon_shop import AmazonPage


@mark.amazon
def test_buy_itemes(driver):
  amazon = AmazonPage(driver)
  amazon.homepage()
  amazon.department_dropdown.find()
  amazon.department_dropdown.click()
  amazon.book_department.find()
  amazon.book_department.click()
  amazon.search_box.send_keys('A Party to Remember')
  
def test_buy_iteme1s(driver):
  amazon = AmazonPage(driver)
  amazon.homepage()