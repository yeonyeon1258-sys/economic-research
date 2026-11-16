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

def save_news(filename, news_list):
    with open(filename, "w", encoding="utf-8") as f:
        for n in news_list:
            f.write(n["title"] + "\n")

result = filter_news(news,"삼성")
save_news("samsung.txt", result)