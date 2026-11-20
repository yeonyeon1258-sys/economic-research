import feedparser

url = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"
feed = feedparser.parse(url)

print(len(feed.entries))

print(feed.entries[0]["title"])

for item in feed.entries:
    print(item["title"])

for item in feed.entries:
    print( item["published"] + " | " +item["title"])