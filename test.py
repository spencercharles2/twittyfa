import tweepy
import twitter_auth
import csv,os

auth = tweepy.OAuthHandler(twitter_auth.API_key, twitter_auth.API_key_secret)
auth.set_access_token(twitter_auth.Access_token, twitter_auth.Access_token_secret)

api = tweepy.API(auth)

tweets = api.home_timeline(screen_name='PankeSa2', result_type='popular',count=50,page=10)

with open('output.csv','w',newline='',encoding='utf8') as csvfile:
    fieldnames = ['url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    for tweet in tweets:
        if tweet.favorite_count > 50:
            #writer.writerow({'url':f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"})
            os.system('telegram-send '+f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
            os.system('telegram-send ' + str(tweet.favorite_count))
            


