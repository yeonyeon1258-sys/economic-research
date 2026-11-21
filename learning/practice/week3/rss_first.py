import feedparser

url = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"
feed = feedparser.parse(url)

print(len(feed.entries))

print(feed.entries[0]["title"])

for item in feed.entries:
    print(item["title"])

for item in feed.entries:
    print( item["published"] + " | " +item["title"])

def count_company(news_list, company):
    count = 0
    for n in news_list:
        if company in n["title"]:
            count = count + 1
    
    return count

print(count_company(feed.entries, "부정"))
print(count_company(feed.entries, "대통령"))

count = 1
for m in feed.entries:
   count = count + 1    
   print( str(count)  + ". " + m["title"])

    
