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

for window in range(0,4):
    
    # 강의정보 팝업으로 이동
    elem = browser.find_elements(By.CLASS_NAME,"lec_kor")[window]
    elem.click()
    print(browser.window_handles)
    browser.switch_to.window( browser.window_handles[window+1] )

    # 강의 정보 가져오기
    soup = BeautifulSoup(browser.page_source,'lxml')
    # data_rows = soup.find_all("table")[0].find("tbody").find_all("tr")[0]
    row = soup.find_all("table")[0].find("tbody").find_all("tr")[0]
    columns = row.find_all("td")
    data = [column.get_text().strip() for column in columns] 
    print(data)


    # 교재 정보 가져오기
    data_rows = soup.find_all("table")[6].find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        data = [column.get_text().strip() for column in columns] 
        print(data)
        # writer.writerow(data)
        
    # 다시 원래 페이지로 돌아가기
    browser.switch_to.window(browser.window_handles[0])

    
browser.quit()