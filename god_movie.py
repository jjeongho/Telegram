
import requests

import time

from bs4 import BeautifulSoup

import telepot



bot = telepot.Bot(token='1210533819:AAFRupwIS-v5JLRzK2WVt4OUStaEqtQhyS4')

chat_id='1182157482'
channel_id ='@ringaroundDmoonhalf'


if __name__ == '__main__':
    # 제일 최신 게시글의 번호 저장
    latest_num = 0
    while True:
        req = requests.get('http://www.coindeskkorea.com/news/articleList.html?view_type=sm')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        article_list = soup.find("section", {"class" : "article-list-content type-sm text-left"})
        article_link = article_list.find("a").attrs['href']

        # 최신글만 30초마다 크롤링
        # latest_num이랑 articel_link가 중복시 아무 반응 없고, 다르면 새로운 뉴스 나옴
        if latest_num != article_link :
            latest_num = article_link
            link = 'http://www.coindeskkorea.com'+ article_link
            req = requests.get(link)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.find("div", {"class" : "article-head-title"}).text
            new_article = '<코인데스크 코리아>'+'\n'+title + '\n'+link
            bot.sendMessage(chat_id, new_article)
            # 프롬프트 로그
            print(link)
            print(title)
        time.sleep(30) # 30초 간격으로 크롤링
        print('링크 : http://www.coindeskkorea.com' + latest_num)
        print(title)