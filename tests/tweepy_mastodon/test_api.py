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


def test_media_upload(twitter_api: tweepy.API, mocker):
    # TODO: write test with mock
    pass


def test_destroy_status(twitter_api: tweepy.API):
    # TODO: write test with mock
    # twitter_api.destroy_status(status_id)
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
        twitter_api.get_user(-1)


def test_user_timeline(twitter_api: tweepy.API):
    statuses = twitter_api.user_timeline(user_id=1, count=1)
    assert len(statuses) == 1
    assert statuses[0].user.screen_name
    assert type(statuses[0].text) is str


def test_get_status(twitter_api: tweepy.API):
    # 'Hello from tweepy-mastodon!'
    # ref. https://mastodon.social/@shuuji3/109813536848077879
    status_id = 109813536848077879
    status = twitter_api.get_status(id=status_id)
    assert status.user.screen_name == 'shuuji3'
    assert 'Hello from tweepy-mastodon!' in status.text
    with pytest.raises(AttributeError):
        status.user.status


def test_destroy_favorite(twitter_api: tweepy.API):
    # 'Hello from tweepy-mastodon!'
    # ref. https://mastodon.social/@shuuji3/109813536848077879
    status_id = 109813536848077879
    status = twitter_api.destroy_favorite(id=status_id)
    assert not status.favorited

    with pytest.raises(Exception):
        twitter_api.destroy_favorite(id=-1)


def test_create_favorite(twitter_api: tweepy.API):
    # 'Hello from tweepy-mastodon!'
    # ref. https://mastodon.social/@shuuji3/109813536848077879
    status_id = 109813536848077879
    status = twitter_api.create_favorite(id=status_id)
    assert status.favorited

    with pytest.raises(Exception):
        twitter_api.create_favorite(id=-1)


def test_retweet(twitter_api: tweepy.API):
    # 'Hello from tweepy-mastodon!'
    # ref. https://mastodon.social/@shuuji3/109813536848077879
    status_id = 109813536848077879
    status = twitter_api.retweet(id=status_id)
    assert status.retweeted

    with pytest.raises(Exception):
        twitter_api.retweet(id=-1)


def test_unretweet(twitter_api: tweepy.API):
    # TODO implement without disruption
    pass


def test_create_friendship(twitter_api: tweepy.API):
    relationship = twitter_api.create_friendship(screen_name='shuuji3@takahe.social', follow=True)
    assert relationship.following

    with pytest.raises(Exception):
        twitter_api.create_friendship(user_id=-1)


def test_destroy_friendship(twitter_api: tweepy.API):
    # TODO implement without disruption
    # relationship = twitter_api.destroy_friendship(screen_name='shuuji3@takahe.social')
    # assert not relationship.following

    with pytest.raises(Exception):
        twitter_api.destroy_friendship(user_id=-1)


def test_create_mute(twitter_api: tweepy.API):
    # TODO implement without disruption
    # user = twitter_api.create_mute(screen_name='shuuji3@takahe.social')
    # assert user

    with pytest.raises(Exception):
        twitter_api.create_mute(user_id=-1)


def test_destroy_mute(twitter_api: tweepy.API):
    user = twitter_api.destroy_mute(screen_name='shuuji3@takahe.social')
    assert user

    with pytest.raises(Exception):
        twitter_api.destroy_mute(user_id=-1)


def test_create_block(twitter_api: tweepy.API):
    # TODO implement without disruption
    # user = twitter_api.create_block(screen_name='shuuji3@takahe.social')
    # assert user

    with pytest.raises(Exception):
        twitter_api.create_block(user_id=-1)


def test_destroy_block(twitter_api: tweepy.API):
    user = twitter_api.destroy_block(screen_name='shuuji3@takahe.social')
    assert user

    with pytest.raises(Exception):
        twitter_api.destroy_block(user_id=-1)
