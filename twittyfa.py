from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import pickle

from time import sleep
import os.path

class twittyfa:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome('./chromedriver.exe')

    def twitter_login(self):
        
        if(os.path.isfile('./twitterCookies.plk') == True):
            print('Cookies Exist! Skiping login')
            self.browser.get('https://twitter.com/')

            print('Importing Cookies ...')
            sleep(2)

            cookies = pickle.load(open('twitterCookies.plk','rb'))

            for line in cookies:
                self.browser.add_cookie(line)
            print('Cookies Has been Imported.')
            
            self.browser.refresh()
            sleep(60)



        else:
            self.browser.get('https://twitter.com/login')
            print('Waiting ...')
            sleep(2)
            
            usernameField = self.browser.find_element_by_name('session[username_or_email]')
            passwordField = self.browser.find_element_by_name('session[password]')

            usernameField.send_keys(self.username)
            passwordField.send_keys(self.password)
            passwordField.send_keys(Keys.ENTER)
            
            print('Waiting ...')
            sleep(2)

            cookiefile = open('twitterCookies.plk' ,'wb')
            print('Cookie file created, dumping data.')
            pickle.dump(self.browser.get_cookies(), cookiefile)
            print('Cookies has been dumped!')
            cookiefile.close()




### یوزرنیم و پسورد را از کاربر دریافت کن
bot = twittyfa('WorstPlayer32@gmail.com','TFItt3RJfeNm*s9XPrEqgL^7q')
bot.twitter_login()

bot.


# actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

