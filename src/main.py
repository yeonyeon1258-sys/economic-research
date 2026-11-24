#import
import csv
import feedparser
from urllib.parse import quote

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

company = "SK 하이닉스"
url = make_search_url(company)    
feed = feedparser.parse(url)        
news = make_news_list(feed.entries)     
save_csv("save.csv", news)    
print("저장 완료: " + str(len(news)) + "건") 

