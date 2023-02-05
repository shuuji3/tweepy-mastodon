import os

import pytest

import tweepy_mastodon as tweepy


@pytest.fixture
def mastodon_credentials():
    mastodon_api_base_url = os.environ.get('MASTODON_API_BASE_URL')
    mastodon_client_id = os.environ.get('MASTODON_CLIENT_ID')
    mastodon_client_secret = os.environ.get('MASTODON_CLIENT_SECRET')
    mastodon_access_token = os.environ.get('MASTODON_ACCESS_TOKEN')
    return mastodon_client_id, mastodon_client_secret, mastodon_access_token, mastodon_api_base_url,


def test_auth(mastodon_credentials):
    mastodon_client_id, mastodon_client_secret, mastodon_access_token, mastodon_api_base_url = mastodon_credentials

    auth = tweepy.OAuth1UserHandler(
        consumer_key=mastodon_client_id,
        consumer_secret=mastodon_client_secret,
        access_token=mastodon_access_token,
        api_base_url=mastodon_api_base_url,
    )

    api = tweepy.API(auth)
    assert api.verify_credentials().screen_name == 'shuuji3'
    assert api.verify_credentials().username == 'shuuji3'


def test_set_access_token(mastodon_credentials):
    mastodon_client_id, mastodon_client_secret, mastodon_access_token, mastodon_api_base_url = mastodon_credentials

    auth = tweepy.OAuth1UserHandler(
        consumer_key=mastodon_client_id,
        consumer_secret=mastodon_client_secret,
        api_base_url=mastodon_api_base_url,
    )
    auth.set_access_token(mastodon_access_token)

    api = tweepy.API(auth)
    assert api.verify_credentials().screen_name == 'shuuji3'
    assert api.verify_credentials().username == 'shuuji3'
