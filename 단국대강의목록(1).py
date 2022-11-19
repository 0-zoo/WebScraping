import time
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

url = "https://webinfo.dankook.ac.kr/tiac/univ/lssn/lpci/views/lssnPopup/tmtbl.do"
browser.get(url) # url로 이동

# 전공 검색 클릭
elem = browser.find_element(By.XPATH,"//*[@id='lpciSearch']/div[1]/table/tbody/tr/td/div[3]/div[2]/input[2]")
elem.click()

# search 클릭
elem = browser.find_element(By.XPATH,"//*[@id='btn_search']/strong")
elem.click()

time.sleep(1)

filename = "단국대강의목록.csv"
f = open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)
title = "수강조직	학년	이수구분	교과목번호	교과목명	분반	원어	학점	교강사	요일/교시/강의실	변경내역	수업방법 및 비고	수업유형".split("\t")
writer.writerow(title)

soup = BeautifulSoup(browser.page_source,'lxml')

data_rows = soup.find("table",attrs={"class":"tbl_mixed tbl_click"}).find("tbody").find_all("tr")

for row in data_rows:
    strikes = row.find_all('a') # a태그 추출
    for strike in strikes:
        row.a.extract()
    columns = row.find_all("td")
    # if len(columns) <= 1: # 의미 없는 데이터는 skip
    #     continue
    # print(columns)
    data = [column.get_text().strip() for column in columns] 
    # print(data)
    writer.writerow(data)
    
browser.quit()