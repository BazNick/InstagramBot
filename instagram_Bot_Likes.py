from selenium import webdriver
from selenium.webdriver.common.by import By
import password
import time

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')

time.sleep(5)

user_mail = browser.find_element_by_css_selector('input[type="text"]')
user_password = browser.find_element_by_css_selector('input[type="password"]')

# enter your login
user_mail.send_keys(password.my_login)
# enter your password
user_password.send_keys(password.my_password)
browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

time.sleep(3)

browser.find_element_by_class_name('cmbtv').click()
time.sleep(3)
browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

target_user = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
# instead of ... type the user your want to find
target_user.send_keys('...')
time.sleep(3)

# instead of ... choose the user from the list and find him/her by link text
browser.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a').click()

time.sleep(5)

# here I find the number of total post and convert string number into int type
# then I divide total number of posts by 10 to scroll down to the bottom of the page
# and to get all the posts
number_of_posts = int(browser.find_element_by_class_name('g47SY').text)
scrolling_formula = number_of_posts // 10

all_images = None

for i in range(0, scrolling_formula):
    all_images = browser.find_elements(By.CLASS_NAME, '_9AhH0')
    browser.execute_script('window.scrollBy(0, document.body.scrollHeight)')
    time.sleep(1)

all_images.pop().click()
time.sleep(1)

number = 0

while number <= number_of_posts:
    get_color = browser.find_element_by_class_name('fr66n').find_element_by_tag_name('svg').get_attribute('fill')
    if get_color == '#262626':
        browser.find_element_by_class_name('fr66n').find_element_by_tag_name('svg').click()
    if number == number_of_posts:
        break
    else:
        browser.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
    time.sleep(2)
    number += 1

time.sleep(3)
browser.close()
