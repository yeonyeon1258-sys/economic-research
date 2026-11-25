#import
import csv
import feedparser
from urllib.parse import quote
from datetime import date
#function

def make_search_url(company):
    keyword = quote(company)
    url ="https://news.google.com/rss/search?q=" + keyword + "&hl=ko&gl=KR&ceid=KR:ko"
    return url

def make_news_list(entries):
    picked = []
    for n in entries:
        news = {"date": n["published"], "title": n["title"], "source": n["source"]["title"]}
        picked.append(news)

    return picked

def save_csv(filename, news_list):
    with open(filename, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "source", "title"])
        writer.writeheader()
        for n in news_list:
            writer.writerow(n)

#run

company = input("기업 이름을 입력하세요: ")
url = make_search_url(company)    
feed = feedparser.parse(url)        
news = make_news_list(feed.entries)
today = str(date.today())
filename = "output/" + company + "_" + today + ".csv"
save_csv(filename, news)
print("저장 완료: " + str(len(news)) + "건") 