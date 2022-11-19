# 파이썬 활용 능력 실기 시험 문제

print("=" *100)
print(" 파이썬 프로그램 활용 능력 실기 시험 문제")
print("=" *100)
###########################################################################################################
# Stage 1. 데이터 수집용 웹크롤러 만들기
###########################################################################################################

###########################################################################################################
# 반드시 아래 지시사항을 숙지한 후 시험에 응시하세요 !!
# 문제 : 아래의 Step 3의 42번행과 Step 5의 68번 행 view_list  부분의 코드를 완성하여 
# 웹 크롤러를 실행하여 데이터를 수집한 후 저장하여 결과물을 제출하세요.
# 시험에 대한 자세한 내용은 주어진 별도의 시험지를 참고하세요
# 제출 과제 누락시 실격처리가 되며 모든 책임은 응시자에게 있습니다.
###########################################################################################################

#Step 1. 필요한 모듈과 라이브러리를 로딩하고 검색어를 입력 받습니다
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys        
import math    

#필요한 정보를 입력 받습니다
query_txt = "여름여행"
cnt = 50
page_cnt = math.ceil(cnt / 10)  # 크롤링 할 페이지 수 
f_name = "c:\\py_temp\\2208-00138이영주.txt"

#Step 2. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
path = "C:\\Users\\gram\\Desktop\\python\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get('http://www.naver.com')
time.sleep(2)

s_time = time.time( )     # 검색을 시작하는 시점의 timestamp 를 지정합니다

#Step 3. 네이버 검색창에 입력 받은 검색어를 넣고 검색을 실행합니다

element = driver.find_element('id','query')# 이곳에 들어갈 적절한 코드를 완성하세요
element.send_keys(query_txt)
element.submit()

#Step 4. 아래의 VIEW 링크를 선택합니다
driver.find_element_by_link_text("VIEW").click( )

#Step 5. 현재 페이지의 내용을 저장 목록을 만든 후 목록에 있는 내용을 파일에 저장하기
no = 1

# 자동 스크롤다운 함수
def scroll_down(driver):
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
  time.sleep(5)

i = 1
while (i <= page_cnt):
      scroll_down(driver) 
      i += 1
    

print("\n")

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

view_list = soup.find('ul', 'lst_total _list_base').find_all('li')

for i in view_list:

    f = open(f_name, 'a',encoding='UTF-8')

    # 게시글 내용
    contents = i.find('div','total_wrap api_ani_send').get_text().replace("\n","")                                  
    f.write(str(no)+": 내용 :" + str(contents) + "\n")
    print(no,": 내용 : %s" %contents)

    f.close( )

    no += 1

    if no > cnt :
        break
        
    print("\n")
    
    time.sleep(1)        # 페이지 변경 전 2초 대기 

#Step 6. 요약 정보를 출력합니다
e_time = time.time( )     # 검색이 종료된 시점의 timestamp 를 지정합니다
t_time = e_time - s_time

print("\n") 
print("=" *80)
print("크롤링을 요청한 총 %s 건 중에서 %s 건의 데이터를 수집 완료 했습니다" %(cnt,no-1))
print("총 소요시간은 %s 초 입니다 " %round(t_time,1))
print("파일 저장 완료: txt 파일명 : %s " %f_name)
print("=" *80)