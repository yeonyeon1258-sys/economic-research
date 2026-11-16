news = [
    {"title": "반도체 수출 증가", "source": "연합"},
    {"title": "HBM 공급 확대", "source": "한경"},
]

def get_first_title(news_list):
    return news_list[0]["title"]

result = get_first_title(news)
print("첫 뉴스:"+ result)