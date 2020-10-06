import requests
import telepot
import time
from bs4 import BeautifulSoup




token = '1210533819:AAFRupwIS-v5JLRzK2WVt4OUStaEqtQhyS4'#봇을 만들시 제공하는 API 토큰입니다!
StartMsg = "Ellipti에서 뉴스를 전해드립니다!" #알아서 멘트 변경하시면 됩니다!""안에만 건들면 됩니당!


def main(msg):
    msg_type, chat_type, chat_id, msg_data, msg_id = telepot.glance(msg, long=True)
    latest_num = 0
    if msg_type == 'text':
        if msg['text'] == '/' + 'Ellipti': #이 단축키 또한 알아서 변경하시면 됩니다!''안에만 건들면 됩니당
            bot.sendMessage(chat_id, StartMsg)# 시작 메시지 제거하고 싶으면 StartMsg 없애면 됩니당
            print(msg)
            while True:
                req = requests.get('http://www.coindeskkorea.com/news/articleList.html?view_type=sm')
                html = req.text
                soup = BeautifulSoup(html, 'html.parser')
                article_list = soup.find("section", {"class": "article-list-content type-sm text-left"})
                article_link = article_list.find("a").attrs['href']

                # 최신글만 30초마다 크롤링
                # latest_num이랑 articel_link가 중복시 아무 반응 없고, 다르면 새로운 뉴스 나옴
                if latest_num != article_link:
                    latest_num = article_link
                    link = 'http://www.coindeskkorea.com' + article_link
                    req = requests.get(link)
                    html = req.text
                    soup = BeautifulSoup(html, 'html.parser')
                    title = soup.find("div", {"class": "article-head-title"}).text
                    new_article = '<코인데스크 코리아aax www>' + '\n' + title + '\n' + link # 이 멘트 또한 마음에 안들면 바꾸시면 됩니당!
                    bot.sendMessage(chat_id, new_article)
                    # 프롬프트 로그
                    print(link)
                    print(title)
                time.sleep(30)  # 30초 간격으로 크롤링 이 값바꾸면 시간 바뀌니깐 알아서 바꾸시면 됩니다!
                print('링크 : http://www.coindeskkorea.com' + latest_num)
                print(title)
            else:
                bot.sendMessage(chat_id, text='새로운 뉴스 없음')

bot = telepot.Bot(token)
bot.message_loop(main,run_forever=True)