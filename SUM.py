import tweepy
import telepot
import time

# 봇 사용 토큰
token = '1153547283:AAHv4fkuGuburI-1ZNMrNm-6nHYDOVjPHp4'  # 봇을 만들시 제공하는 API 토큰입니다
StartMsg = "Ellipti에서 트위터 실시간 트윗을 보여드립니다!"  # 알아서 멘트 변경하시면 됩니다!""안에만 건들면 됩니당!
Info = '\n' + "\n더 자세히 알아보고 싶다면?\n " + "https://twitter.com/"

screen_name1 = "kava_labs"  # 트위터 @ID


consumer_key = "W6HRtryg7NoLmVFIbgMPXI6yF"

consumer_secret = "CEdCrB8sv8dq3uKRansHNB7ifLlEIDuIal63e4QuiKH9BXSjTM"

access_token = "1186470858744745984-KXlNpXKgB9tUS5lHjfcOTfTtHLRRaV"

access_token_secret = "IEsYIFxje2YJl38qSZ8tSG4yAOvGgYdf3sqlmj8GRtWU6"


def main(msg):
    msg_type, chat_type, chat_id, msg_data, msg_id = telepot.glance(msg, long=True)
    latest_num1 = 0

    if msg_type == 'text':
        if msg['text'] == '/' + 'twit':  # 이 단축키 또한 알아서 변경하시면 됩니다!''안에만 건들면 됩니당
            bot.sendMessage(chat_id, StartMsg)  # 시작 메시지 제거하고 싶으면 StartMsg 없애면 됩니당
            print(msg)

            while True:
                if msg_type == 'text':
                    if msg['text'] == '/' + 'end':
                        end_twit = '종료'
                        bot.sendMessage(chat_id, end_twit)  # 시작 메시지 제거하고 싶으면 StartMsg 없애면 됩니당
                        print(msg)
                        break
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)
                statuses1 = api.user_timeline(screen_name1, count=1, Tweet_mode="extended")


                for status in statuses1:
                    if (not status.retweeted) and ('RT @' not in status.text):
                        if latest_num1 != status.text:
                            latest_num1 = status.text
                            new_twit = '✉️새로운 KAVA 트윗이 도착했습니다✉️\n\n' + status.text + Info + screen_name1 + "\n" + "\n한국 공식 커뮤니티 채널 : https://t.me/kava_korea"
                            bot.sendMessage(chat_id, new_twit)

                time.sleep(30)



        else:
            if msg['text'] == '/' + '엘립티':
                print(msg)



bot = telepot.Bot(token)
bot.message_loop(main, run_forever=True)