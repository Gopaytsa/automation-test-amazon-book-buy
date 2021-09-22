from pytest import mark
from pages.amazon.amazon_shop import AmazonPage


@mark.amazon
def test_buy_itemes(driver):
  amazon = AmazonPage(driver)
  amazon.homepage()
  amazon.department_dropdown.find()
  amazon.department_dropdown.click()
  amazon.book_department.go_to_element('Books')
  amazon.search_box.click()
  amazon.search_box.input_text('A Party to Remember')
  amazon.search_box.sumbit_action()
  amazon.select_item.find()
  assert amazon.select_item.text() == 'Bronco and Friends: A Party to Remember'
  amazon.select_item.click()
  amazon.add_to_cart.find()
  item_1 = amazon.item_page_price.text()
  amazon.add_to_cart.click()
  assert int(amazon.check_cart.text()) == 1
  assert amazon.check_total_sum_in_cart.text() == item_1
  amazon.search_box.click()
  amazon.search_box.input_text('Baby University')
  amazon.search_box.sumbit_action()
  amazon.select_specific_item.find()
  assert amazon.select_specific_item.text() == 'Baby University Complete "for Babies" Board Book Set (Baby University Board Book Sets)'
  amazon.select_specific_item.click()
  item_2 = amazon.item_page_price.text()
  amazon.add_to_cart.find()
  amazon.add_to_cart.click()
  assert int(amazon.check_cart.text()) == 2
  total_sum_1 = float(amazon.check_total_sum_in_cart.text()[1:])
  assert total_sum_1 == round((float(item_1[1:]) + float(item_2[1:])), 2)
  amazon.go_to_cart.click()
  assert amazon.shopping_cart_page.text() == 'Shopping Cart'
  items = amazon.items_names_in_cart_on_cart_page.get_elements_text_list()
  shop_list = ['Baby University Complete "for Babies" Board Book Set (Baby University Board Book Sets)', 
              'Bronco and Friends: A Party to Remember']
  assert shop_list == items
  items_prices = amazon.items_prices_in_cart_on_cart_page.get_elements_text_list()
  assert items_prices == [item_2, item_1]
  amazon.get_gift.checkbox()
  assert amazon.get_gift.is_check_box_selected() == True
  amazon.change_quantity_of_first_item.chenge_quantity('3')
  assert amazon.current_quantity_of_first_item.check_actual_qty_first_item() == '3'
  new_item_2_price = items_prices[0]
  assert item_2 == new_item_2_price
  total_sum_2 = amazon.total_sum.text()
  float(total_sum_2[2:]) > total_sum_1
  amazon.checkout_order.find()
  amazon.checkout_order.click()
  amazon.sign_in_page.find()
  assert amazon.sign_in_page.text() == 'Sign-In'

  
  
