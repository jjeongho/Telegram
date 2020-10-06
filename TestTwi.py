import tweepy

# assign the values accordingly
consumer_key = "W6HRtryg7NoLmVFIbgMPXI6yF"

consumer_secret = "CEdCrB8sv8dq3uKRansHNB7ifLlEIDuIal63e4QuiKH9BXSjTM"

access_token = "1186470858744745984-KXlNpXKgB9tUS5lHjfcOTfTtHLRRaV"

access_token_secret = "IEsYIFxje2YJl38qSZ8tSG4yAOvGgYdf3sqlmj8GRtWU6"

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

# screen name of the account to be fetched
screen_name = "patriamea"

# number of statuses to be fetched
count = 3

# fetching the statuses
statuses = api.user_timeline(screen_name, count=count)

# printing the statuses
for status in statuses:
    print(status.text, end="\n\n")
print(str(len(statuses)) + " number of statuses have been fetched.")
