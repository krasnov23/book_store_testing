import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")


#проскролить на 600 px
driver.execute_script("window.scrollBy(0, 600);")

ruby_btn = driver.find_element(By.XPATH,'//*[@id="text-22-sub_row_1-0-2-0-0"]/div/ul/li/a[1]/h3').click()
reviews = driver.find_element(By.XPATH,'//*[@id="product-160"]/div[3]/ul/li[2]/a').click()
five_stars_btn = driver.find_element(By.CLASS_NAME,'star-5').click()

add_review_field = driver.find_element(By.ID,'comment')
add_review_field.send_keys('Nice book!')
author_field = driver.find_element(By.ID,'author')
author_field.send_keys('Boris')
email_field = driver.find_element(By.ID,'email')
email_field.send_keys('crasnov.boris@yandex.ru')

submit_btn = driver.find_element(By.ID,'submit').click()

driver.quit()