import csv

news = [
    {"date": "2026-11-22", "source": "한국경제", "title": "반도체 수출 증가"},
    {"date": "2026-11-22", "source": "연합뉴스", "title": "환율 하락, 수출 기업 부담"}

]

def save_csv(filename, news_list):
    with open(filename, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "source", "title"])
        writer.writeheader()
        for n in news_list:
            writer.writerow(n)
        
save_csv("test2.csv", news)

save_csv("test3.csv", [news[0]])