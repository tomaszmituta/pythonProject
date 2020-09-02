from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

chromedriver_path = 'C:/Users/tomas/PycharmProjects/pythonProject/Instagram/chromedriver.exe'  # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(10)
webdriver.get('https://www.linkedin.com/')
sleep(3)


username = webdriver.find_element_by_name('session_key')
#enter yor e-mail
username.send_keys('tomasz.mituta@gmail.com')
password = webdriver.find_element_by_name('session_password')
#enter pass to linkied in
password.send_keys('Tomasz01+')

#enter to page
login_in_enter = webdriver.find_element_by_name("session_password").send_keys(Keys.RETURN)

sleep(5)
search=webdriver.find_element_by_xpath(
                '/html/body/header/div/form/div/div/div/div/div/div/input')

sleep(5)
search.send_keys("#skills #sap #sd #job")
sleep(5)
search.send_keys(Keys.RETURN)
sleep(5)
#job search
job_click=webdriver.find_element_by_xpath(
                '/html/body/div[8]/div[3]/div/div/header/div/div/div/ul/li[2]/button/span')
sleep(5)
job_click.click()
sleep(4)
#job search by the location
job_search_by_location =webdriver.find_element_by_xpath(
                '/html/body/header/div/form/div/div/div/div/div[3]/div/div/input')
sleep(5)
job_search_by_location.clear()
sleep(1)
job_search_by_location.send_keys("usa")
sleep(4)
#job_search_by_location.send_keys(Keys.RETURN)
Search_click =webdriver.find_element_by_xpath(
                 '/html/body/header/div/form/div/div/div/div/button')
sleep(3)
Search_click.click()








