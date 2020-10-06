import tweepy

# 트위터 Application에서 발급 받은 key 정보들

consumer_key = "W6HRtryg7NoLmVFIbgMPXI6yF"

consumer_secret = "CEdCrB8sv8dq3uKRansHNB7ifLlEIDuIal63e4QuiKH9BXSjTM"

access_token = "1186470858744745984-KXlNpXKgB9tUS5lHjfcOTfTtHLRRaV"

access_token_secret = "IEsYIFxje2YJl38qSZ8tSG4yAOvGgYdf3sqlmj8GRtWU6"

# 1. 핸들러 생성 및 개인정보 인증요청
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# 2. 액세스 요청
auth.set_access_token(access_token, access_token_secret)

# 3. twitter API 생성
api = tweepy.API(auth)

keyword = 'KAVA'  # 검색하고 싶은 키워드 입력
result = []  # 크롤링 텍스트를 저장 할 리스트 변수

for i in range(1, 3):  # 1,2 페이지 크롤링
    tweets = api.search(keyword)  # keyword 검색 실시. 결과가 tweets 변수에 담긴다.
    for tweet in tweets:
        result.append([tweet.id_str, tweet.text, tweet.created_at])  # 크롤링 결과 리스트에 삽입.(id, 트윗내용, 생성날짜)

print(len(result))  # 크롤링하여 가져온 트윗 개수
print(result[0])  # 수집결과 확인(첫번째 항목만)
# print(result) # 전체를 확인하고 싶으면 이 코드로