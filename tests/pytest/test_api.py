import os
import sys

from mastodon import Mastodon
import pytest

import tweepy_mastodon as tweepy


@pytest.fixture
def twitter_api() -> tweepy.API:
    consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
    consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
    access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuth1UserHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
    auth.set_access_token(key=access_token, secret=access_token_secret)

    yield tweepy.API(auth)


@pytest.fixture
def mastodon_api() -> Mastodon:
    api_base_url = os.environ.get('MASTODON_API_BASE_URL')
    client_id = os.environ.get('MASTODON_CLIENT_ID')
    client_secret = os.environ.get('MASTODON_CLIENT_SECRET')
    access_token = os.environ.get('MASTODON_ACCESS_TOKEN')

    if not (client_id and client_secret and access_token):
        print('environment variable not found!')
        sys.exit(1)

    yield Mastodon(client_id, client_secret, access_token, api_base_url=api_base_url)


def test_twitter_api(twitter_api):
    assert twitter_api.verify_credentials().screen_name == 'shuuji3'


def test_mastodon_api(mastodon_api: Mastodon):
    assert mastodon_api.me().username == 'shuuji3'
