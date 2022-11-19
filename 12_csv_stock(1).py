import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200(1).csv"
f = open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)
title = "N  종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)

for page in range(1,5): # 1부터 5페이지까지
    res = requests.get(url + str(page)) # 페이지별로 url 다르게 넣어줌&page는 숫자 데이터이므로 문자열 데이터로 변환해줘야 함
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    data_rows = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr") # 행은 tr 단위로 되어있음
    for row in data_rows: # 행의 마지막까지 반복
        columns = row.find_all("td") # 열은 tr 안의 모든 td
        if len(columns)<=1: # 페이지 내에서 간격을 띄우기 위한 무의미한 데이터 삭제
            continue
        data = [column.get_text().strip() for column in columns] # 반복문을 한 문장에서 실행, 리스트 하나에 한 행의 내용을 모두 담아서 개행 제거
        print(data)
        writer.writerow(data)
            





    
    
    
