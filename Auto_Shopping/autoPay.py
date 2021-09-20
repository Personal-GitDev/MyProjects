#!/bin/python3.6
import requests
import json
from selenium import webdriver
import time

print('Loading sniper...')
r = requests.get('https://feature.com/products.json')
products = json.loads((r.text))['products']

for product in products:
        #print(product['title'])
        productname = product['title']
       
        if productname == 'Adidas Originals x Pharrell Williams Basics Hoodie - Black':
                producturl = 'https://feature.com/products/' + product['handle']
                        #return producturl
                print('Adidas Originals x Pharrell Williams Basics Hoodie - Black') 

driver = webdriver.Chrome(executable_path=r'/home/europa/chromedriver')
driver.get(producturl)
time.sleep(1.5)
print('Adding to basket...')
driver.find_element_by_xpath('//button[@class="primary-btn add-to-cart"]').click()
print('Basket Complete!')
time.sleep(1.5)
#driver.find_element_by_xpath('//button[@class="btn btn-solid"]').click()
driver.get('https://feature.com/checkout')
print('Filling in address...')
driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('thisemail@hotmail.com')
time.sleep(1)
driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys('Timmy')
time.sleep(1)
driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys('Turner')
time.sleep(1)
driver.find_element_by_xpath('//input[@placeholder="Address"]').send_keys('61 Cotlandswick')
time.sleep(1)
driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys('London Colney')
time.sleep(1)
s1 = driver.find_element_by_xpath("//select[@size='1']")   
s1.send_keys('United States')
time.sleep(1)
s2 = driver.find_element_by_xpath("//select[@placeholder='State']")
s2.send_keys('Alabama')
time.sleep(1)
driver.find_element_by_xpath('//input[@placeholder="ZIP code"]').send_keys('35011')
time.sleep(1)
driver.find_element_by_xpath('//input[@type="tel"]').send_keys('01727506327')
driver.find_element_by_xpath('//button[@id="continue_button"]').click()
print('Address complete!')
time.sleep(6)
driver.find_element_by_xpath('//button[@id="continue_button"]').click()
print('Filling in payment...')
#driver.find_element_by_xpath('//input[@type="tel"]').send_keys('4958 1979 2970 7816')
#time.sleep(1)
#driver.find_element_by_xpath('//input[@id="name"]').send_keys('T Turner')
#time.sleep(1)
#driver.find_element_by_xpath('//input[@id="number"]').send_keys('1022')
#time.sleep(1)
#driver.find_element_by_xpath('//input[@id="verification_value"]').send_keys('855')
#print('Payment complete!')
#time.sleep(1)
#driver.find_element_by_xpath('//span[@class="btn_content"]').click()
#print('Didnt snipe this time unlucky!')
