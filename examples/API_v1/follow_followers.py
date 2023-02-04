import tweepy_mastodon


consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy_mastodon.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy_mastodon.API(auth)

# Follow every follower of the authenticated user
for follower in tweepy_mastodon.Cursor(api.get_followers).items():
    follower.follow()
