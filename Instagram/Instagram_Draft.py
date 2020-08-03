from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


def likeandcomment():
    # Liking the picture
    button_like = webdriver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div[1]/article/div[2]/section[1]/span[1]/button/span')
    button_like.click()
    likes = likes + 1
    sleep(randint(15, 30))
    # commenting the photo
    webdriver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div[1]/article/div[2]/section[1]/span[2]/button/span').click()
    sleep(randint(15, 30))
    comm = webdriver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div[1]/article/div[2]/section[3]/div[1]/form/textarea')
    sleep(10)
    comm.send_keys(
        'This is Great! Like your profile! Check out my profile, if you like it, follow and like it :) Hope to get your support! Keep The Good Work!:')
    sleep(10)
    comm.send_keys(Keys.ENTER)
    sleep(20)
    # Next pic
    webdriver.find_element_by_link_text('Dalej').click()
    sleep(randint(15, 30))
    print(likes)


chromedriver_path = 'C:/Users/tomas/PycharmProjects/Repo_Learning/Web_Scraping/chromedriver.exe'  # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('tomasz.mituta@gmail.com')
password = webdriver.find_element_by_name('password')
password.send_keys('Widzew01+')

login_in_enter = webdriver.find_element_by_name("password").send_keys(Keys.RETURN)

sleep(3)

alert_no = webdriver.find_element_by_class_name("mt3GC")
alert_no.click()

hashtag_list = ['traveler', 'landscape', 'drone', 'dronephotos', 'dronephotography', 'goprophotography',
                'traveldestination',
                'photographer', 'vacation', 'instatravel', 'travelblogger', 'photooftheday',
                'instapic', 'inspiration', 'instacool', 'happiness', 'blogger', 'travel',
                'follow', 'me', 'art', 'style']
# hashtag_list = ['fashion','follow','me','art','style','family','amazing','bestoftheday','nice','landscape','photographer','vacation','instagramers','instatravel']

prev_user_list = []  # - if it's the first time you run it, use this line and comment the two below
# prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,
#               1:2]  # useful to build a user log
# prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
    sleep(5)
    first_thumbnail = webdriver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

    first_thumbnail.click()
    sleep(randint(1, 5))
    try:
        if
            for likes in range(1, 90):
                likeandcomment()


    except:
        continue

    else:
        print("good job")

print("Final Job")
