import time
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
url = "https://webinfo.dankook.ac.kr/tiac/univ/lssn/lpci/views/lssnPopup/tmtbl.do"
browser.get(url)

# 전공 검색 클릭
browser.find_element(By.XPATH,"//*[@id='lpciSearch']/div[1]/table/tbody/tr/td/div[3]/div[2]/input[2]").click()
# search 클릭
browser.find_element(By.XPATH,"//*[@id='btn_search']/strong").click()

for window in range(0,5):
    time.sleep(1)
    # 강의정보 팝업으로 이동
    browser.find_elements(By.CLASS_NAME,"lec_kor")[window].click()
    
    browser.switch_to.window( browser.window_handles[1] )

    browser.close()

    time.sleep(1)
    
    browser.switch_to.window(browser.window_handles[0])

time.sleep(1)
browser.quit()