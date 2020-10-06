import tweepy
import telepot
import time
from bs4 import BeautifulSoup

#봇 사용 토큰
token = '1153547283:AAHv4fkuGuburI-1ZNMrNm-6nHYDOVjPHp4'#봇을 만들시 제공하는 API 토큰입니다
StartMsg = "Ellipti에서 트위터 실시간 트윗을 보여드립니다!" #알아서 멘트 변경하시면 됩니다!""안에만 건들면 됩니당!

screen_name = "patriamea" #트위터 @ID


# assign the values accordingly
consumer_key = "W6HRtryg7NoLmVFIbgMPXI6yF"

consumer_secret = "CEdCrB8sv8dq3uKRansHNB7ifLlEIDuIal63e4QuiKH9BXSjTM"

access_token = "1186470858744745984-KXlNpXKgB9tUS5lHjfcOTfTtHLRRaV"

access_token_secret = "IEsYIFxje2YJl38qSZ8tSG4yAOvGgYdf3sqlmj8GRtWU6"

def main(msg):
    msg_type, chat_type, chat_id, msg_data, msg_id = telepot.glance(msg, long=True)
    latest_num = 0
    if msg_type == 'text':
        if msg['text'] == '/' + 'Ellipti': #이 단축키 또한 알아서 변경하시면 됩니다!''안에만 건들면 됩니당
            bot.sendMessage(chat_id, StartMsg)# 시작 메시지 제거하고 싶으면 StartMsg 없애면 됩니당
            print(msg)
            count = 1
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)
            statuses = api.user_timeline(screen_name, count=count)


            for status in statuses:
                bot.sendMessage(chat_id,status.text)
            print(" ****** "+str(len(statuses)) + "개의 트윗을 가져왔습니다. ****** ")


        else:
            bot.sendMessage(chat_id, text='새로운 뉴스 없음')

bot = telepot.Bot(token)
bot.message_loop(main,run_forever=True)