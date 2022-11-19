import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) # url로 이동

time.sleep(1)

# 가는 날 클릭
browser.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[7]/button/b").click()

time.sleep(1)

#8/27, 8/30일 선택
# class="sc-crXcEl gjxYDG inner"
# //*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[3]
# browser.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[7]/button").click()

time.sleep(1)
