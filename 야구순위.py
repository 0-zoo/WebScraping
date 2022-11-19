import requests
from bs4 import BeautifulSoup
import csv

url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo&year=2021"

filename = "야구순위2015-2022.csv"
f = open(filename,"w",encoding="utf8",newline="")
writer = csv.writer(f)
title = "순위	팀	경기수	승	패	무	승률	게임차	연속	출루율	장타율	최근10경기".split(" ")
writer.writerow(title)

for page in range(2015,2022):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    data_rows = soup.find("table",attrs={"cellspacing":"0"}).find("tbody").find_all("tr") # 행은 tr 단위로 되어있음
    
    for row in data_rows: # 행의 마지막까지 반복
        ranks = row.find("strong")
        columns = row.find_all("td") # 열은 tr 안의 모든 td
        if len(columns)<=1: # 페이지 내에서 간격을 띄우기 위한 무의미한 데이터 삭제
            continue
        rank = ranks.get_text().strip()
        data = [rank] + [ column.get_text().strip() for column in columns ] # 반복문을 한 문장에서 실행, 리스트 하나에 한 행의 내용을 모두 담아서 개행 제거
        print(data)
        writer.writerow(data)
    writer.writerow("")