news = [
    {"title": "반도체 수출 증가", "source": "연합"},
    {"title": "HBM 공급 확대", "source": "한경"},
    {"title": "금리 동결 전망", "source": "한경"},
]


def get_by_source(news_list, source):
    picked = []
    for n in news_list:
        if n["source"] == source:
            picked.append(n)
    
    return picked

result = get_by_source(news,"연합")

for item in result:
    print(item["title"])

