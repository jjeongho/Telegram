import tweepy
import telepot
import time

# 봇 사용 토큰
token = '1153547283:AAHv4fkuGuburI-1ZNMrNm-6nHYDOVjPHp4'  # 봇을 만들시 제공하는 API 토큰입니다
StartMsg = "Ellipti에서 트위터 실시간 트윗을 보여드립니다!"  # 알아서 멘트 변경하시면 됩니다!""안에만 건들면 됩니당!
Info = '\n' + "\n더 자세히 알아보고 싶다면?\n " + "https://twitter.com/"

screen_name1 = "kava_labs"  # 트위터 @ID
screen_name2 = "getprotocol"
screen_name3 = "tokamak_network"
screen_name4 = "GUTStickets"
screen_name5 = "synthetix_io"
screen_name6 = "InjectiveLabs"
screen_name7 = "cartesiproject"
screen_name8 = "JakChung"

consumer_key = "W6HRtryg7NoLmVFIbgMPXI6yF"

consumer_secret = "CEdCrB8sv8dq3uKRansHNB7ifLlEIDuIal63e4QuiKH9BXSjTM"

access_token = "1186470858744745984-KXlNpXKgB9tUS5lHjfcOTfTtHLRRaV"

access_token_secret = "IEsYIFxje2YJl38qSZ8tSG4yAOvGgYdf3sqlmj8GRtWU6"


def main(msg):
    msg_type, chat_type, chat_id, msg_data, msg_id = telepot.glance(msg, long=True)
    latest_num1 = 0
    latest_num2 = 0
    latest_num3 = 0
    latest_num4 = 0
    latest_num5 = 0
    latest_num6 = 0
    latest_num7 = 0
    latest_num8 = 0

    if msg_type == 'text':
        if msg['text'] == '/' + 'twit':  # 이 단축키 또한 알아서 변경하시면 됩니다!''안에만 건들면 됩니당
            bot.sendMessage(chat_id, StartMsg)  # 시작 메시지 제거하고 싶으면 StartMsg 없애면 됩니당
            print(msg)

            while True:
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)
                statuses1 = api.user_timeline(screen_name1, count=1, Tweet_mode="extended")
                statuses2 = api.user_timeline(screen_name2, count=1, Tweet_mode="extended")
                statuses3 = api.user_timeline(screen_name3, count=1, Tweet_mode="extended")
                statuses4 = api.user_timeline(screen_name4, count=1, Tweet_mode="extended")
                statuses5 = api.user_timeline(screen_name5, count=1, Tweet_mode="extended")
                statuses6 = api.user_timeline(screen_name6, count=1, Tweet_mode="extended")
                statuses7 = api.user_timeline(screen_name7, count=1, Tweet_mode="extended")
                statuses8 = api.user_timeline(screen_name8, count=1, Tweet_mode="extended")

                for status in statuses1:
                    if (not status.retweeted) and ('RT @' not in status.text):
                        if latest_num1 != status.text:
                            latest_num1 = status.text
                            new_twit = '✉️새로운 KAVA 트윗이 도착했습니다✉️\n\n' + status.text + Info + screen_name1 + "\n" + "\n한국 공식 커뮤니티 채널 : https://t.me/kava_korea"
                            bot.sendMessage(chat_id, new_twit)

                for status in statuses2:
                    if (not status.retweeted) and ('RT @' not in status.text):
                        if latest_num2 != status.text:
                            latest_num2 = status.text
                            new_twit = '✉️새로운 GET 트윗이 도착했습니다✉️\n\n' + status.text + Info + screen_name2 + "\n" + "\n한국 공식 커뮤니티 채널 : https://t.me/getkorea"
                            bot.sendMessage(chat_id, new_twit)

                for status in statuses3:
                    if (not status.retweeted) and ('RT @' not in status.text):
                        if latest_num3 != status.text:
                            latest_num3 = status.text
                            new_twit = '✉️새로운 TOKAMAK 트윗이 도착했습니다✉️\n\n' + status.text + Info + screen_name3 + "\n" + "\n 공식 커뮤니티 채널 :https://t.me/tokamak_network"
                            bot.sendMessage(chat_id, new_twit)

                for status in statuses4:
                    if (not status.retweeted) and ('RT @' not in status.text):
                        if latest_num4 != status.text:
                            latest_num4 = status.text
                            new_twit = '✉️새로운 GUTSTICKETS 트윗이 도착했습니다✉️\n\n' + status.text + Info + screen_name4 + "\n" + "\n한국 공식 커뮤니티 채널 : https://t.me/getkorea"
                            bot.sendMessage(chat_id, new_twit)

                for status in statuses5:
                    if (not status.retweeted) and ('RT @' not in status.text):
                        if latest_num5 != status.text:
                            latest_num5 = status.text
                            new_twit = '✉️새로운 SYNTHETIX 트윗이 도착했습니다✉️\n\n' + status.text + Info + screen_name5 + "\n" + "\n한국 공식 커뮤니티 채널 : https://t.me/SYNTHETIX_KOREA"
                            bot.sendMessage(chat_id, new_twit)

                for status in statuses6:
                    if (not status.retweeted) and ('RT @' not in status.text):
                        if latest_num6 != status.text:
                            latest_num6 = status.text
                            new_twit = '✉️새로운 INJECTIVE 트윗이 도착했습니다✉️\n\n' + status.text + Info + screen_name6 + "\n" + "\n한국 공식 커뮤니티 채널 : https://t.me/Injective_Korea"
                            bot.sendMessage(chat_id, new_twit)

                for status in statuses7:
                    if (not status.retweeted) and ('RT @' not in status.text):
                        if latest_num7 != status.text:
                            latest_num7 = status.text
                            new_twit = '✉️새로운 CARTESI 트윗이 도착했습니다✉️\n\n' + status.text + Info + screen_name7 + "\n" + "\n한국 공식 커뮤니티 채널 : https://t.me/CartesiKR"
                            bot.sendMessage(chat_id, new_twit)

                for status in statuses8:
                    if (not status.retweeted) and ('RT @' not in status.text):
                        if latest_num8 != status.text:
                            latest_num8 = status.text
                            new_twit = '✉️새로운 JakChung 트윗이 도착했습니다✉️\n\n' + status.text + Info + screen_name8+ "\n" + "\n한국 공식 커뮤니티 채널 : https://t.me/JakChung"
                            bot.sendMessage(chat_id, new_twit)

                time.sleep(30)
        else:
            if msg['text'] == '엘립티':
                print(msg)



bot = telepot.Bot(token)
bot.message_loop(main, run_forever=True)