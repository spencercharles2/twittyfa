import tweepy
import twitter_auth
import csv,os
import time

auth = tweepy.OAuthHandler(twitter_auth.API_key, twitter_auth.API_key_secret)
auth.set_access_token(twitter_auth.Access_token, twitter_auth.Access_token_secret)

api = tweepy.API(auth)

tweets = api.home_timeline(screen_name='PankeSa2', result_type='popular',count=300, page=10)

def get_popular_tw():
    with open('output.csv','w',newline='',encoding='utf8') as csvfile:
        fieldnames = ['url','likes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        tw_dict = dict()

        for tweet in tweets:
            if tweet.favorite_count > 35 and tweet.lang == 'fa':
                #tw_dict[tweet.favorite_count] = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
                #writer.writerow({'url':f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"})
                #os.system('telegram-send '+f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
                #os.system('telegram-send ' + str(tweet.favorite_count))
                
                print(str(tweet.favorite_count) + " == " + f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
                
            #time.sleep(15)
            #get_popular_tw()


while True:
    get_popular_tw()
    print('waiting 5 seconds')
    time.sleep(5)