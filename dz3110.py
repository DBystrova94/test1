import time

def awesome_func():
  x = 5
  while x != 0:
    y = 0
    y = y + x
    x = x - 1
  return (y)


def awesome_func1():
  y = 3
  while y != 5:
    y += 1
  return (y)

#
awesome_func()  #Вызов функции
#awesome_func1()
print(awesome_func())


# by Alex
class TestElements:
  class TestTextBox:

    def test_text_box(self, driver):
      text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
      text_box_page.open()
      text_box_page.fill_all_fields()
      output_name, output_email, output_current, output_permanent = text_box_page.check_field_form()
      print(output_name)
      print(output_email)
      print(output_current)
      print(output_permanent)
      time.sleep(5)

