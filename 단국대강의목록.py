import csv
import requests
from bs4 import BeautifulSoup

url = "https://webinfo.dankook.ac.kr/tiac/univ/lssn/lpci/views/lssnPopup/tmtbl.do"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

filename = "단국대강의목록.csv"
f = open(filename,"w",encoding="utf8",newline="")
writer = csv.writer(f)
title = "수강조직	학년	이수구분	교과목번호	교과목명	분반	원어	학점	교강사".split("\t")
writer.writerow(title)

data_rows = soup.find("table",attrs={"class":"tbl_mixed tbl_click"}).find("tbody").find_all("tr")
for row in data_rows:
    columns = row.find_all("td")
    # if len(columns) <= 1: # 의미 없는 데이터는 skip
    #     continue
    data = [column.get_text().strip() for column in columns]
    print(data)
    # writer.writerow(data)

    