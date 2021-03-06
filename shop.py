import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)
my_account_menu_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-50"]/a').click()

# SHOP отображение страницы товара
username = driver.find_element(By.ID,'username')
username.send_keys('crasnov.boris@yandex.ru')
password = driver.find_element(By.ID,'password')
password.send_keys('Krasnov123.')
login_btn = driver.find_element(By.XPATH,'//*[@id="customer_login"]/div[1]/form/p[3]/input[3]').click()
shop_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-40"]/a').click()

#скрол вниз для поиска нужного элемента
driver.execute_script("window.scrollBy(0, 600);")
html_5forms_btn = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[3]/a[1]/h3').click()
html_5forms_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "product_title.entry-title"), "HTML5 Forms"))

#SHOP кол-во товаров в категории

driver.execute_script("window.open();")# открытие новой вкладки
window_after = driver.window_handles[1]# создание переменной, где укажем путь к второй вкладке (window_handles[1]) ; здесь будет 1, так как отсчёт начинается с 0
driver.switch_to.window(window_after) # переключим область действия драйвера на новую вкладку, теперь дальнейшие элементы драйвер будет искать уже там
driver.get("http://practice.automationtesting.in/")


my_account_menu_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-50"]/a').click()
shop_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-40"]/a').click()
# поля внизу не требуются т.к аккаунт авторизован, но на случай если авторизации нету пусть будет
#username = driver.find_element(By.ID,'username')
#username.send_keys('crasnov.boris@yandex.ru')
#password = driver.find_element(By.ID,'password')
#password.send_keys('Krasnov123.')
#login_btn = driver.find_element(By.XPATH,'//*[@id="customer_login"]/div[1]/form/p[3]/input[3]').click()
html_category_btn = driver.find_element(By.XPATH,'//*[@id="woocommerce_product_categories-2"]/ul/li[2]/a').click()

check_amount_html = driver.find_elements(By.CSS_SELECTOR,'.products.masonry-done > li')
assert len(check_amount_html) == 3


#shop сортировка товаров
driver.execute_script("window.open();")# открытие новой вкладки
window_after = driver.window_handles[2]# создание переменной, где укажем путь к второй вкладке (window_handles[1]) ; здесь будет 1, так как отсчёт начинается с 0
driver.switch_to.window(window_after) # переключим область действия драйвера на новую вкладку, теперь дальнейшие элементы драйвер будет искать уже там
driver.get("http://practice.automationtesting.in/")

shop_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-40"]/a').click()
selector = driver.find_element(By.CLASS_NAME,'orderby').click()
check_selector = driver.find_element(By.CSS_SELECTOR,"[value='menu_order']")
check_attribute = check_selector.get_attribute('selected')
assert check_attribute is not None

element = driver.find_element(By.CLASS_NAME,"orderby") # "element" это просто название переменной, можно задать и другое
select = Select(element) # Select после "=" должен быть с большой буквы, так как в import он указан с большой буквы
select.select_by_value("price") # ищем элемент с текстом "Sales" ; в этом и предыдущем методе добавлять .click() не нужно

selector = driver.find_element(By.CLASS_NAME,'orderby').click()
check_selector = driver.find_element(By.CSS_SELECTOR,"[value='price']")
check_attribute = check_selector.get_attribute('selected')
assert check_attribute is not None



# SHOP Отображение скидка товара
driver.execute_script("window.open();")# открытие новой вкладки
window_after = driver.window_handles[3]# создание переменной, где укажем путь к второй вкладке (window_handles[1]) ; здесь будет 1, так как отсчёт начинается с 0
driver.switch_to.window(window_after) # переключим область действия драйвера на новую вкладку, теперь дальнейшие элементы драйвер будет искать уже там
driver.get("http://practice.automationtesting.in/")

shop_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-40"]/a').click()
android_book = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[1]/a[1]/h3')
# прокрутка до нужного аргумента в нашем случае android_book
driver.execute_script("return arguments[0].scrollIntoView(true);", android_book)
android_book.click()

old_price = driver.find_element(By.XPATH,'//*[@id="product-169"]/div[2]/div[1]/p/del/span')
assert old_price.text == '₹600.00'
new_price = driver.find_element(By.XPATH,'//*[@id="product-169"]/div[2]/div[1]/p/ins/span')
assert new_price.text == '₹450.00'

image_click = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product-169"]/div[1]/a/img')) )
image_click.click()
close_image = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')) )
close_image.click()


#SHOP проверка цены в корзине.
driver.execute_script("window.open();")# открытие новой вкладки
window_after = driver.window_handles[4]# создание переменной, где укажем путь к второй вкладке (window_handles[1]) ; здесь будет 1, так как отсчёт начинается с 0
driver.switch_to.window(window_after) # переключим область действия драйвера на новую вкладку, теперь дальнейшие элементы драйвер будет искать уже там
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

shop_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-40"]/a').click()
#html_wd = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[4]/a[2]')
#driver.execute_script("return arguments[0].scrollIntoView(true);", html_wd)
html_wd_click = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/ul/li[4]/a[2]')) )

html_wd = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[4]/a[2]').click()

time.sleep(7)

items = driver.find_element(By.CLASS_NAME,'cartcontents')
assert items.text == '1 Item'
amount = driver.find_element(By.XPATH,'//*[@id="wpmenucartli"]/a/span[2]')
assert amount.text == '₹180.00'
amount.click()


subtotal = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH,
'//*[@id="page-34"]/div/div[1]/div/div/table/tbody/tr[1]/td/span'), "180.00"))
total = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH,
'//*[@id="page-34"]/div/div[1]/div/div/table/tbody/tr[3]/td/strong/span'), "189.00"))

# SHOP работа в корзине

driver.execute_script("window.open();")# открытие новой вкладки
window_after = driver.window_handles[1]# создание переменной, где укажем путь к второй вкладке (window_handles[1]) ; здесь будет 1, так как отсчёт начинается с 0
driver.switch_to.window(window_after) # переключим область действия драйвера на новую вкладку, теперь дальнейшие элементы драйвер будет искать уже там
driver.get("http://practice.automationtesting.in/")


shop_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-40"]/a').click()
driver.execute_script("window.scrollBy(0, 300);")
html_wd = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[4]/a[2]').click()
html5_webd = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[4]/a[2]').click()
time.sleep(3)

js_data_structures = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[5]/a[2]').click()
items_btn = driver.find_element(By.XPATH,'//*[@id="wpmenucartli"]/a/span[2]').click()

time.sleep(2)
delete_book = driver.find_element(By.XPATH,'//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[1]/a').click()

und_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-34"]/div/div[1]/div[1]/a')) )
und_btn.click()


quantity_js_field = driver.find_element(By.XPATH,'//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input')
# очищаем поле
quantity_js_field.clear()
quantity_js_field.send_keys(3)
update_basket_btn = driver.find_element(By.XPATH,'//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[3]/td/input[1]').click()

quantity_js_field = driver.find_element(By.XPATH,'//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input')
amount_of_book = quantity_js_field.get_attribute('value')
assert amount_of_book == '3'

time.sleep(5)
apply_coupon = WebDriverWait(driver, 20,).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.coupon > .button')) )
apply_coupon.click()

#apply_coupon_btn = driver.find_element(By.CSS_SELECTOR,'.coupon > .button').click()
time.sleep(3)
please_enter_coupon_msg = driver.find_element(By.XPATH,'//*[@id="page-34"]/div/div[1]/ul/li')
#please_enter_coupon_msg = driver.find_element(By.CSS_SELECTOR,'.woocommerce-error > li')

assert please_enter_coupon_msg.text == 'Please enter a coupon code.'

# SHOP покупка товара

pesonal_data = {
    'billing_first_name' : 'Boris',
    'billing_last_name' : 'Krasnov',
    'billing_email' : 'crasnov.boris@yandex.ru',
    'billing_phone' : '89297169752',
    'billing_address_1' : 'Tolyatti',
    'billing_city' : 'Tolyatti',
    'billing_state' : 'Samara state',
    'billing_postcode' : '445040'
}

driver.execute_script("window.open();")# открытие новой вкладки
window_after = driver.window_handles[2]# создание переменной, где укажем путь к второй вкладке (window_handles[1]) ; здесь будет 1, так как отсчёт начинается с 0
driver.switch_to.window(window_after) # переключим область действия драйвера на новую вкладку, теперь дальнейшие элементы драйвер будет искать уже там
driver.get("http://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 300);")
shop_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-40"]/a').click()
basket = driver.find_element(By.CLASS_NAME,'wpmenucart-contents').click()
proceed_to_checkout = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-34"]/div/div[1]/div/div/div/a')) )
proceed_to_checkout.click()

for field,data in pesonal_data.items():
    send_data = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, field)))
    #send_data = driver.find_element(By.ID,field)
    send_data.send_keys(data)

country_field = driver.find_element(By.ID,'select2-chosen-1').click()
country_enter_field = driver.find_element(By.CLASS_NAME,'select2-input.select2-focused')
country_enter_field.send_keys('Russia')
#russia = driver.find_element(By.CSS_SELECTOR,'[value = "RU"]').click()
#country_enter_field.send_keys(Keys.ENTER)
russia_choose =  driver.find_element(By.ID,'select2-results-1').click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 600);")

check_payments_btn = driver.find_element(By.ID,'payment_method_cheque')
check_payments_btn.click()

place_ord_btn = driver.find_element(By.ID,'place_order')
place_ord_btn.click()

time.sleep(7)
end_of_purchase = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

check_payments_text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-35"]/div/div[1]/table/tfoot/tr[3]/td'),"Check Payments"))













































