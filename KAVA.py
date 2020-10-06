import tweepy
import telepot
import time
from bs4 import BeautifulSoup

#봇 사용 토큰
token = '828332844:AAH271soyjq5jhG85Qf1muAunVcuOHEM-h8'#봇을 만들시 제공하는 API 토큰입니다
StartMsg = "Ellipti에서 지금부터 트위터 실시간 트윗을 보여드립니다!" #알아서 멘트 변경하시면 됩니다!""안에만 건들면 됩니당!

screen_name = "JakChung" #트위터 @ID


# assign the values accordingly
consumer_key = "W6HRtryg7NoLmVFIbgMPXI6yF"

consumer_secret = "CEdCrB8sv8dq3uKRansHNB7ifLlEIDuIal63e4QuiKH9BXSjTM"

access_token = "1186470858744745984-KXlNpXKgB9tUS5lHjfcOTfTtHLRRaV"

access_token_secret = "IEsYIFxje2YJl38qSZ8tSG4yAOvGgYdf3sqlmj8GRtWU6"

def main(msg):
    msg_type, chat_type, chat_id, msg_data, msg_id = telepot.glance(msg, long=True)
    latest_num = 0

    if msg_type == 'text':
        if msg['text'] == '/' + 'twit': #이 단축키 또한 알아서 변경하시면 됩니다!''안에만 건들면 됩니당
            bot.sendMessage(chat_id, StartMsg)# 시작 메시지 제거하고 싶으면 StartMsg 없애면 됩니당
            print(msg)
            while True:
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)
                statuses = api.user_timeline(screen_name, count=1)


                for status in statuses:
                    if (not status.retweeted) and ('RT @' not in status.text):
                        if latest_num != status.text:
                            latest_num = status.text
                            new_twit = '<새로 업데이트 된 트윗>' + '\n' + status.text + '\n'+"\n더 자세히 알아보고 싶다면?\n "+"https://twitter.com/" +screen_name    # 이 멘트 또한 마음에 안들면 바꾸시면 됩니당!
                            bot.sendMessage(chat_id, new_twit)
                            print(" ****** " + str(len(statuses)) + "개의 새로운 트윗을 가져왔습니다. ****** ")
                            print(status.text)
                time.sleep(30)

        else:
            bot.sendMessage(chat_id, text='새로운 뉴스 없음')

bot = telepot.Bot(token)
bot.message_loop(main,run_forever=True)