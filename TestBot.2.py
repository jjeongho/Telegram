import feedparser

feed = feedparser.parse("https://www.coindesk.com/feed/")

coindesk_urls = [] #coindesk url들을 가져와서 저장시켜줄 객체

for entry in feed['entries']:
    coindesk_urls.append(entry['link']) #coindesk_url  list에  entries에 들어 있는 link 의 string들을 추가한다.

for url in coindesk_urls:
    with open("coindesk_news.txt", "a", encoding="utf8") as f:
        f.write(url+"\n")