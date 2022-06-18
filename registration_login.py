import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)

# регистрация аккаунта.
my_account_menu_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-50"]/a').click()
# Почта crasnov.boris@yandex.ru , пароль Krasnov123.
email_field = driver.find_element(By.ID,'reg_email')
email_field.send_keys('crasnov.boris@yandex.ru')
password_field = driver.find_element(By.ID,'reg_password')
password_field.send_keys('Krasnov123.')
register_btn = driver.find_element(By.XPATH,'//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').click()
time.sleep(3)
password_field.send_keys('..')
register_btn = driver.find_element(By.XPATH,'//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').click()
#register_work_btn = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "reg_password")) )


# заход под своим логином
driver.execute_script("window.open();")# открытие новой вкладки
window_after = driver.window_handles[1]# создание переменной, где укажем путь к второй вкладке (window_handles[1]) ; здесь будет 1, так как отсчёт начинается с 0
driver.close()
driver.switch_to.window(window_after) # переключим область действия драйвера на новую вкладку, теперь дальнейшие элементы драйвер будет искать уже там
driver.get("http://practice.automationtesting.in/") # на новой вкладке откроем какую-нибудь другую страницу на сайте
my_account_menu_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-50"]/a').click()
username = driver.find_element(By.ID,'username')
username.send_keys('crasnov.boris@yandex.ru')
password = driver.find_element(By.ID,'password')
password.send_keys('Krasnov123.')
login_btn = driver.find_element(By.XPATH,'//*[@id="customer_login"]/div[1]/form/p[3]/input[3]').click()
logout_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-36"]/div/div[1]/nav/ul/li[6]/a')) )








# заход на сайт через форму логина и пароля.











