news = [
    {"date" : "2026-10-30", "title" : "한화비전 3분기 실적 발표", "source" : "예시"},
    {"date" : "2026-10-29", "title" : "한화비전, 3Q 영업이익 1026억", "source" : "뉴스1"},
    {"date" : "2026-10-29", "title" : "한화비전, 보안·반도체 장비 힘입어 영업익 183.3% ‘껑충’", "source" : "서울경제"}
]

def save_news():
    with open("filename", "w", encoding="utf-8") as file:
        for item in news:
            file.write("[" + item["date"] + "] "+ item["title"] + "(출처: " + item["source"] + ")""\n")

save_news()