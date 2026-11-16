# 경제 뉴스 데이터 연습
company = "한화비전" 

news = [
    "한화비전 3분기 실적 발표",
    "글로벌 보안 시장 성장",
    "AI 영상 분석 기술 확대"
]

print("기업명 :", company)

print("주요 뉴스 목록:")

for item in news:
    print("-", item)

with open("news.txt", "w", encoding="utf-8") as file:
    for item in news:
        file.write(item + "\n")

print("뉴스 파일 저장 완료!")

print("\n저장된 뉴스 다시 읽기")

with open("news.txt", "r", encoding="utf-8") as file:
    saved_news = file.readlines()

for item in saved_news:
    print(item.strip())