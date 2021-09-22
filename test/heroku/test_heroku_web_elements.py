from pytest import mark
from pages.heroku.heroku import Heroku

@mark.heroku
def test_heroku_dropdown_option(driver):
  heroku = Heroku(driver)
  heroku.homepage()
  heroku.dropdown.click()
  assert heroku.dropdown_list.current_page_url() == 'http://the-internet.herokuapp.com/dropdown'
  heroku.dropdown_list.go_to_element('Option 2')
  assert heroku.second_option.text() == 'Option 2'
  assert heroku.dropdown_list.attribute('value') == '2'
  
  
@mark.parallel
def test_find_qux_button(driver):
  heroku = Heroku(driver)
  heroku.homepage()
  heroku.challenging_dom.click()
  assert heroku.dropdown_list.current_page_url() == 'http://the-internet.herokuapp.com/challenging_dom'
  heroku.buttons.click_second_button()  
  heroku.button_qux.find()
  assert heroku.button_qux.text() == 'qux', "Button 'qux' not displayed" 


@mark.parallel
def test_find_foo_button(driver):
  heroku = Heroku(driver)
  heroku.homepage()
  heroku.challenging_dom.click()
  assert heroku.button_foo.text() == 'foo', "Button 'foo' not displayed" 


@mark.parallel
def test_find_definebas1(driver):
  heroku = Heroku(driver)
  heroku.homepage()
  heroku.challenging_dom.click()
  assert heroku.dropdown_list.current_page_url() == 'http://the-internet.herokuapp.com/challenging_dom'
  heroku.find_table_cell.find()
  assert heroku.find_table_cell.text() == 'Definiebas1'

  
@mark.parallel
def test_find_delete(driver):
  heroku = Heroku(driver)
  heroku.homepage()
  heroku.challenging_dom.click()
  assert heroku.dropdown_list.current_page_url() == 'http://the-internet.herokuapp.com/challenging_dom'
  heroku.find_table_cell.find()
  assert heroku.find_cell_in_row.text() == 'delete'
