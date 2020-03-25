from selenium import webdriver
import os
from time import sleep

email = 'shikhar.p@somaiya.edu'
password = 'xHFT2020@'

class TradeBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=os.path.abspath(r"C:/Users/shikh/Downloads/Setups_Zip_files/chromedriver.exe"))

    def login(self):
        self.driver.get('https://moneybhai.moneycontrol.com/')

        sleep(2)

        continue_btn = self.driver.find_element_by_xpath('//*[@id="myButton"]')
        continue_btn.click()

        skip_btn = self.driver.find_element_by_xpath('//*[@id="intro4"]/a')
        skip_btn.click()

        play_btn = self.driver.find_element_by_xpath('//*[@id="loginbtn"]')
        play_btn.click()

        '''
        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click() '''
