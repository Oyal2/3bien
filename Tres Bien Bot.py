__author__ = 'Oyal2'
from random import getrandbits
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def cook(amt):
     for i in range(1, amt + 1):
        url = 'http://updates.tres-bien.com/t/d/s/ciuddh/';
        s = requests.session()
        email = 'youremail+{}@gmail.com'.format(getrandbits(40));
        payload = {
            'cm-name': '',#Full Name
            'cm-ciuddh-ciuddh': email,
            'cm-f-palyt': '',#Address
            'cm-f-palyi': '',#Zip Code
            'cm-f-palyd': '',#City
            'cm-fo-palyh': '', #<-- COUNTRY CODE
            'cm-f-palyk': '',#Phone Number
            'cm-fo-palyu': '',#<-- SHOE SIZE CODE
        }
        proxies = {
          #'http': 'http://10.10.1.10:3128', format should be like this
          #'http': 'socks5://user:pass@host:port',
        }
        '''
            USE THESE SIZE CODES FOR cm-fo-palyu
                    1931853 = US 8
                    1931854 = US 8,5
                    1931855 = US 9
                    1931856 = US 9,5
                    1931857 = US 10
                    1931858 = US 10,5
                    1931859 = US 11
                    1931860 = US 11,5
                    1931861 = US 12
                    1931862 = US 12,5
                    1931863 = US 13
            USE THESE COUNTRIES FOR cm-f-palyk
                    1931621 = United Kingdom
                    1931622 = United States of America
        '''
        s.post(url, data=payload, proxies=proxies);
        print('Created {}/{} Entries'.format(i,amt))
        time.sleep(2)
     print("Ok now lets wait for all the entries to process!");
     time.sleep(30);
     email = '' #your email
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
        open = driver.find_elements_by_css_selector('div[role=listitem]')
        open[i].click()
        time.sleep(5)
        link = driver.find_elements_by_partial_link_text('http://updates.tres-bien.com/t/d-c')
        link[i].click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
amt = input('How many entries?  ')
cook(int(amt))
