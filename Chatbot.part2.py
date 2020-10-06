import time
import feedparser
import requests
import telepot

API_KEY = '1210533819:AAFRupwIS-v5JLRzK2WVt4OUStaEqtQhyS4'

bot = telepot.Bot(token=API_KEY)  # bot을 선언합니다.


def get_news_article(url):
    from lxml import html
    import requests

    resp = requests.get(url)
    lxml_html = html.fromstring(resp.text)

    # 제목 추출하기
    news_title = [lxml_html.find_class("article-top-image-section-inner")[0].text_content().strip() + "\n\n"]  ##1

    # 본문 추출하기
    lxml_end_point = lxml_html.cssselect("em")
    lxml_end_point = lxml_end_point[0]
    end_parent = lxml_end_point.getparent()

    body_lxml = []
    for elem in end_parent.itersiblings(preceding=True):
        body_lxml.append(elem)

    news_body = [t.text_content() for t in body_lxml[::-1]]

    news_title.extend(news_body)

    return news_title


def text_barn_maker(post_lines, max_char=4000):
    cumulated = 0
    _text = ''
    text_barn = []
    for t in post_lines:
        trim_t = t.strip(' ')[:max_char]  # prevent limit max_char
        cumulated += len(trim_t)

        if cumulated > max_char:
            text_barn.append(_text)
            _text = ''  # text initialize

            cumulated = len(trim_t)  # new text_part
            _text += trim_t
        else:
            _text += trim_t

    text_barn.append(_text)

    return text_barn


def send_news(text_barn):
    print("{} text barn(s)".format(len(text_barn)))
    for text_line in text_barn:
        bot.sendMessage(chat_id="1182157482", text=text_line)  # chat_id는 본인 것으로 변경하셔야 합니다.
    print("well sent")


while True:
    feed = feedparser.parse("https://www.coindesk.com/feed/")
    coindesk_urls = []

    for entry in feed['entries']:
        coindesk_urls.append(entry['link'])

    with open("coindesk_news.txt", "r", encoding="utf8") as f:
        old_urls = f.read().split("\n")

    new_urls = []

    for new in coindesk_urls:  # 새 URL을 new_urls에 추가
        if new not in old_urls:
            new_urls.append(new)
        else:
            pass

for url in new_urls:  # 함수를 통해 실제 동작하는 부분
    news_lines = get_news_article(url)
    news_barn = text_barn_maker(news_lines)
    send_news(news_barn)
    with open("coindesk_news.txt", "a", encoding="utf8") as f:
        f.write(url + "\n")
    print("well sent")
time.sleep(300)