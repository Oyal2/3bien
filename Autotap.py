__author__ = 'Oyal2'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

email = ''#your email
password = ''#put your password in
url = 'https://mail.google.com/mail/u/0/#inbox'
driver = webdriver.Firefox();
driver.get(url);
UserID = driver.find_element_by_id("identifierId")
UserID.send_keys(email)
click = driver.find_element_by_id("identifierNext")
click.click()
time.sleep(2)
PassID = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
PassID.send_keys(password)
click2 = driver.find_element_by_xpath('//*[@id="passwordNext"]')
click2.click()
time.sleep(3)
driver.get('') #Tres Bien order confirm link !!!NOT THE LINK THEY TELL YOU TO PRESS!!!
time.sleep(3)
open = driver.find_elements_by_css_selector('div[role=listitem]')
open[0].click()
link = driver.find_elements_by_partial_link_text('http://updates.tres-bien.com/t/d-c-f')
link[0].click()
driver.switch_to.window(driver.window_handles[0])
for i in range(0, len(open)):
    print(i)
    print(len(open))
    open = driver.find_elements_by_css_selector('div[role=listitem]')
    open[i].click()
    time.sleep(1)
    link = driver.find_elements_by_partial_link_text('http://updates.tres-bien.com/t/d-c')
    link[i].click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)