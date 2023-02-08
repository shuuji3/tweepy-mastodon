import os
import sys

from mastodon import Mastodon
import pytest

import tweepy_mastodon as tweepy


@pytest.fixture
def twitter_api() -> tweepy.API:
    api_base_url = os.environ.get('MASTODON_API_BASE_URL')
    consumer_key = os.environ.get('MASTODON_CLIENT_ID')
    consumer_secret = os.environ.get('MASTODON_CLIENT_SECRET')
    access_token = os.environ.get('MASTODON_ACCESS_TOKEN')

    auth = tweepy.OAuth1UserHandler(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        api_base_url=api_base_url
    )
    auth.set_access_token(access_token)

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


def test_home_timeline(twitter_api: tweepy.API):
    statuses = twitter_api.home_timeline(count=1)
    assert len(statuses) == 1
    assert statuses[0].user.screen_name


def test_update_status(twitter_api: tweepy.API, mocker):
    # TODO: write test with mock
    pass


def test_get_user(twitter_api: tweepy.API):
    user = twitter_api.get_user(user_id=1)
    assert user.id_str == '1'
    assert user.screen_name == 'Gargron'
    assert user.name == 'Eugen Rochko'

    user = twitter_api.get_user(screen_name='npr@mstdn.social')
    assert user.id == 1201325
    assert user.screen_name == 'NPR@mstdn.social'
    assert user.name == 'NPR :verified:'

    with pytest.raises(Exception):
        twitter_api.get_user(None, None)
