from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import time
from time import sleep

start = time.time()

path_shp = "C:/Users/shikh/Downloads/Setups_Zip_files/chromedriver.exe"
email = 'shikhar.p@somaiya.edu'
password = 'xHFT2020@'
stock_name = 'TCS'
quantity = 50

class TradeBot():
    def __init__(self):
        self.driver = webdriver.Chrome(path_shp)

    def login(self):

        self.driver.get('https://moneybhai.moneycontrol.com')

        sleep(2)

        continue_btn = self.driver.find_element_by_xpath('//*[@id="myButton"]')
        continue_btn.click()

        skip_btn = self.driver.find_element_by_xpath('//*[@id="intro4"]/a')
        skip_btn.click()

        play_btn = self.driver.find_element_by_xpath('//*[@id="loginbtn"]')
        play_btn.click()

        self.driver.switch_to.frame("myframe")
        sleep(2)

        email_in = self.driver.find_element_by_xpath("//input[@form-name='login_form' and @name='email']")
        email_in.send_keys(email)

        pwd_in = self.driver.find_element_by_xpath("//input[@form-name='login_form' and @name='pwd']")
        pwd_in.send_keys(password)

        large_login = self.driver.find_element_by_xpath("//button[@id='ACCT_LOGIN_SUBMIT']")
        large_login.click()
        sleep(2)

    def transact(self):

        transact_link = link = self.driver.find_element_by_link_text('Transact')
        transact_link.click()
        sleep(1)

    def input_stock(self):

        input_stock = self.driver.find_element_by_class_name('search-input')
        input_stock.send_keys(stock_name)
        sleep(3)
        add_btn = self.driver.find_element_by_xpath('//*[@id="auto-suggest"]/ul/li/button')
        add_btn.click()
        sleep(3)

    def buy_stock(self):

        buy_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]')
        buy_button.click()

        quantity = self.driver.find_element_by_xpath('//*[@id="AS-BSE"]/div[2]/div[1]/label/input')
        quantity.send_keys(50)

        current_price = self.driver.find_element_by_xpath('//*[@id="txt_mktprice"]').get_attribute('value')
        current_price = float(current_price)
        target = current_price + 15
        stop_loss = current_price - 15
        stop_loss = round(stop_loss,2)

        gtc = Select(self.driver.find_element_by_xpath('//*[@id="gtc_select"]'))
        gtc.select_by_index(1)

        investment_amount = self.driver.find_element_by_id('invest_amt')
        investment_amount.click()

        target_input = self.driver.find_element_by_xpath('//*[@id="target"]')
        target_input.send_keys(str(target))

        stoploss_input = self.driver.find_element_by_xpath('//*[@id="stop_loss"]')
        stoploss_input.send_keys(str(stop_loss))

        submit_butn =  self.driver.find_element_by_xpath('//*[@id="btn_submit"]')
        submit_butn.click()

    def sell_stock(self,selling_link):

    	portfolio_link = self.driver.find_element_by_link_text('Portfolio')
    	portfolio_link.click()

    	port_link = self.driver.find_element_by_xpath('//*[@id="portfolio"]/div/ul/li[2]/a')
    	port_link.click()
    	sleep(1)

    	stocks_link = self.driver.find_element_by_xpath('//*[@id="tib0"]/div[2]/p')
    	stocks_link.click()

    	elems = self.driver.find_elements_by_xpath("//a[@href]")
    	for elem in elems:
    		if elem.get_attribute("href") == selling_link:
    			elem.click()
    		print(elem.get_attribute("href"))

    	#Sell Button
    	#sell_butn =  self.driver.find_element_by_xpath('//*[@id="stocksellBtn"]')
        #sell_butn.click()



bot = TradeBot()
L_start = time.time()
bot.login()
L_end =  time.time()
bot.transact()
I_start = time.time()
bot.input_stock()
bot.buy_stock()
primary_ticker = "HSL01"
selling_link = "https://moneybhai.moneycontrol.com/neworderview/stocks/"+primary_ticker
bot.sell_stock(selling_link)
I_end = time.time()
end = time.time()
print(f"Total Time taken to run script {end - start} seconds")
print(f"Time to login {L_end - L_start} seconds")
print(f"Time to execute trade {I_end - I_start} seconds")
