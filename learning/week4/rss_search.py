import feedparser
from urllib.parse import quote

print(quote("삼성전자"))
print(quote("SK 하이닉스"))

def make_search_url(company):
    keyword = quote(company)
    url ="https://news.google.com/rss/search?q=" + keyword + "&hl=ko&gl=KR&ceid=KR:ko"
    return url

print(make_search_url("삼성전자"))

result = make_search_url("삼성전자")

feed = feedparser.parse(result)
print(len(feed.entries))
print(feed.entries[0]["title"],feed.entries[1]["title"], feed.entries[2]["title"])
