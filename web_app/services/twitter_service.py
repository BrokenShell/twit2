import tweepy
from credentials import Credentials as cr


auth = tweepy.OAuthHandler(cr.twitter_api_key, cr.twitter_api_secret)
auth.set_access_token(cr.twitter_access_token, cr.twitter_access_token_secret)
api = tweepy.API(auth)


if __name__ == "__main__":
    user = api.get_user("Broken36224820")
    print(user.id)
    print(user.screen_name)
    print(user.name)
    print(user.followers_count)

    tweets = api.user_timeline("Broken36224820", tweet_mode="extended", count=150)
    for tweet in tweets:
        print("-----")
        print(tweet.id, tweet.full_text)
