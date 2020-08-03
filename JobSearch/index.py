from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

chromedriver_path = 'C:/Users/tomas/PycharmProjects/All-Projects/Instagram/chromedriver.exe'  # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(10)
webdriver.get('https://www.linkedin.com/')
sleep(3)


username = webdriver.find_element_by_name('session_key')
#enter yor e-mail
username.send_keys('ID')
password = webdriver.find_element_by_name('session_password')
#enter pass to linkied in
password.send_keys('pass')

#enter to page
login_in_enter = webdriver.find_element_by_name("session_password").send_keys(Keys.RETURN)

sleep(5)
search=webdriver.find_element_by_xpath(
                '/html/body/header/div/form/div/div/div/div/div/div/input')

sleep(5)
search.send_keys("#jezierski")
sleep(5)
search.send_keys(Keys.RETURN)
sleep(5)
click_name=webdriver.find_element_by_class_name('name-and-distance')
click_name.click()
sleep(5)
#send Message
send_message=webdriver.find_element_by_xpath(
                '/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div/section/div[2]/div/div[2]/div/div/span[2]/div/div')
sleep(5)
send_message.click()
sleep(5)
# #back
# back_to_search=webdriver.back()
# sleep(5)

#hire will be loop for click_name +1 as this needs run ++1


