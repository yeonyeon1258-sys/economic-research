news = [
    {"title": "삼성전자 HBM 공급 확대", "source": "한경"},
    {"title": "SK하이닉스 실적 호조", "source": "연합"},
    {"title": "삼성바이오 신규 수주", "source": "매경"},
]

def filter_news(news_list, company):
    picked = []
    for n in news_list:
        if  company in n["title"]:
            picked.append(n)
    
    return picked

result = filter_news(news,"하이닉스")

for item in result:
    print(item["title"])