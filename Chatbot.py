import telepot
import requests
import telepot
from bs4 import BeautifulSoup


# 검색 키워드
search_word = '코인'

token = '1210533819:AAFRupwIS-v5JLRzK2WVt4OUStaEqtQhyS4'#위에서 발급받은 토큰 기입

StartMsg =   "암호화폐 관련 뉴스 보고싶어? : news \n" \
            "라고 검색해봐! "

# 기존에 보냈던 링크를 담아둘 리스트
old_links = []





def extract_links(old_links=[]):
    url = f'https://m.search.naver.com/search.naver?where=m_news&sm=mtb_jum&query={search_word}'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    search_result = soup.select_one('#news_result_list')
    news_list = search_result.select('.bx > .news_wrap > a')

    links = []
    for news in news_list[:5]:
        link = news['href']
        links.append(link)

    new_links = []
    for link in links:
        if link not in old_links:
            new_links.append(link)

    return new_links

def main(msg):
    global old_links
    new_links = extract_links(old_links)
    msg_type, chat_type, chat_id, msg_data, msg_id = telepot.glance(msg, long=True)

    if msg_type == 'text':
        if msg['text'] == '/'+'start':
            bot.sendMessage(chat_id, StartMsg)
            print(msg)
        elif msg['text'] == 'news':
            if new_links:
                for link in new_links:
                    bot.sendMessage(chat_id, text=link)
                    print(msg)
            else:
                bot.sendMessage(chat_id, text='새로운 뉴스 없음')
                """old_links += new_links.copy()
                old_links = list(set(old_links))"""



bot = telepot.Bot(token)
bot.message_loop(main,run_forever=True)