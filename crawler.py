from time import sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os 
import time  
import cx_Oracle
   

class Crawler():
    def __init__(self , target_web) :
        self.target_web  = target_web
      
    def get_web(self , options):
        
        # webdriver 操作
        
        driver =webdriver.Chrome(options=options  ,executable_path= os.path.abspath(r'./chromedriver.exe'))
        time.sleep(1)
        driver .get(self.target_web)
        driver.find_element_by_xpath(r'//*[@id="ui-id-2"]').click()
        driver.find_element_by_xpath(r'//*[@id="fileFormatId"]/option[3]').click()
        driver.find_element_by_xpath(r'//*[@id="historySeason_id"]/option[12]').click()
        driver.find_element_by_xpath(r'//*[@id="downloadBtnId"]').click()
        time.sleep(1)

if __name__== '__main__':
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    options.add_argument('--user-agent=%s' % user_agent)
    options.add_argument('--window-size=1920x1080') 
    target_web = r'https://plvr.land.moi.gov.tw/DownloadOpenData'
    print('crawler start ')
    #程式開始處
    Crawler(target_web).get_web(options)
    print('crawler done ')