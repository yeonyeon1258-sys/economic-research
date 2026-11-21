import feedparser

url = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"
feed = feedparser.parse(url)

print(feed.entries[0].keys())
print(feed.entries[0]["source"])

first = feed.entries[0]
one = {"date": first["published"], "title": first["title"], "source": first["source"]["title"]}
print(one)

def make_news_list(entries):
    picked = []
    for n in entries:
        news = {"date": n["published"], "title": n["title"], "source": n["source"]["title"]}
        picked.append(news)

    return picked

news_list = make_news_list(feed.entries)
print(len(news_list))
print(news_list[0])

def filter_news(news_list, company):
    picked = []
    for n in news_list:
        if  company in n["title"]:
            picked.append(n)
    
    return picked

result = filter_news(news_list, "-")
for n in result:
    print(n["source"] + " | " + n["title"])