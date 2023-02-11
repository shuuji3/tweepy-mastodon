import datetime
import os

import tweepy_mastodon as tweepy


def test_example_usage():
    mastodon_api_base_url = os.environ.get('MASTODON_API_BASE_URL')
    mastodon_consumer_key = os.environ.get('MASTODON_CLIENT_ID')
    mastodon_consumer_secret = os.environ.get('MASTODON_CLIENT_SECRET')
    mastodon_access_token = os.environ.get('MASTODON_ACCESS_TOKEN')

    auth = tweepy.OAuth1UserHandler(
        consumer_key=mastodon_consumer_key,
        consumer_secret=mastodon_consumer_secret,
        api_base_url=mastodon_api_base_url
    )
    auth.set_access_token(mastodon_access_token)

    api = tweepy.API(auth)

    me = api.verify_credentials()

    assert me.screen_name == 'shuuji3'
    assert me.display_name == 'TAKAHASHI Shuuji 🌈✨'
    assert me.url == 'https://shuuji3.xyz'
    assert me.profile_background_image_url == 'https://files.mastodon.social/accounts/headers/000/936/436/original/4d6989a698953e80.jpg'
    assert me.created_at == datetime.datetime(2019, 10, 8, 0, 0, tzinfo=datetime.timezone.utc)
    assert me.avatar == 'https://files.mastodon.social/accounts/avatars/000/936/436/original/4854d6cf9e12cb8f.png'

    assert me.status.favorited == False
    assert me.status.retweeted == False

    user_statuses = api.user_timeline(user_id=1, since_id=0, count=1)
    assert len(user_statuses) == 1

    status_id = 109813536848077879  # ref. https://mastodon.social/@shuuji3/109813536848077879
    status = api.get_status(id=status_id)
    assert status.user.screen_name == 'shuuji3'
    assert 'Hello from tweepy-mastodon!' in status.text
