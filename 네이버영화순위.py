import requests
from bs4 import BeautifulSoup
import csv

filename = "크리스마스영화순위2011-2021.csv"
f = open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)
title = "순위	제목".split(" ")
writer.writerow(title)

for year in range(2011,2021):
    url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cnt&tg=0&date={}1225".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    title_rows = soup.find("table",attrs={"class":"list_ranking"}).find("tbody").find_all("tr") 
    count=1;
    for row in title_rows:
        if(count>=11):
            break
        if len(row)<=1:
            continue
        data = [count] + [row.find("a").get_text().strip()]
        print(data)
        writer.writerow(data)
        count = count+1
    print("")
    writer.writerow("")
    