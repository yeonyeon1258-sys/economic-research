samsung_news = [
    {"date": "11/03", "title": "삼성전자 3분기 실적 발표", "source": "연합뉴스"},
    {"date": "11/05", "title": "삼성전자 HBM 공급 확대", "source": "한국경제"}
]
hynix_news = [
    {"date": "11/04", "title": "SK하이닉스 신규 공장 착공", "source": "매일경제"}
]

def save_news(filename, news_list):
    with open(filename, "w", encoding="utf-8") as f:
        for n in news_list:
            f.write(n["date"] + " | " + n["title"] + "\n")

save_news("samsung.txt", samsung_news)
save_news("hynix.txt", hynix_news)