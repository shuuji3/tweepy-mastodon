import datetime
from dateutil.tz import tzutc

import pytest

from tests.pytest.test_api import mastodon_api
from tweepy_mastodon.utils import convert_user


@pytest.fixture
def mastodon_user():
    # mastodon.me()
    yield {
        'id': 936436,
        'username': 'shuuji3',
        'acct': 'shuuji3',
        'display_name': 'TAKAHASHI Shuuji 🌈✨',
        'locked': False,
        'bot': False,
        'discoverable': False,
        'group': False,
        'created_at': datetime.datetime(2019, 10, 8, 0, 0, tzinfo=tzutc()),
        'note': '<p>🧑🏻\u200d💻 software engineer / 🌟 like: opensource, technology, science, beautiful things, something fun, reasonable idea, &amp; fairness</p>',
        'url': 'https://mastodon.social/@shuuji3',
        'avatar': 'https://files.mastodon.social/accounts/avatars/000/936/436/original/4854d6cf9e12cb8f.png',
        'avatar_static': 'https://files.mastodon.social/accounts/avatars/000/936/436/original/4854d6cf9e12cb8f.png',
        'header': 'https://files.mastodon.social/accounts/headers/000/936/436/original/4d6989a698953e80.jpg',
        'header_static': 'https://files.mastodon.social/accounts/headers/000/936/436/original/4d6989a698953e80.jpg',
        'followers_count': 18,
        'following_count': 33,
        'statuses_count': 73,
        'last_status_at': datetime.datetime(2023, 2, 3, 0, 0),
        'noindex': False,
        'source': {
            'privacy': 'public',
            'sensitive': False,
            'language': None,
            'note': '🧑🏻\u200d💻 software engineer / 🌟 like: opensource, technology, science, beautiful things, something fun, reasonable idea, & fairness',
            'fields': [
                {
                    'name': 'Website',
                    'value': 'https://shuuji3.xyz',
                    'verified_at': '2022-11-21T03:44:51.983+00:00',
                },
                {
                    'name': 'GitHub',
                    'value': 'https://github.com/shuuji3',
                    'verified_at': '2022-12-19T17:22:50.150+00:00',
                },
                {
                    'name': 'Takahē testing',
                    'value': 'https://takahe.social/@shuuji3',
                    'verified_at': None,
                },
                {
                    'name': 'Blog',
                    'value': 'https://weblog.shuuji3.xyz',
                    'verified_at': None,
                },
            ],
            'follow_requests_count': 0,
        },
        'emojis': [],
        'fields': [
            {
                'name': 'Website',
                'value': '<a href="https://shuuji3.xyz" target="_blank" rel="nofollow noopener noreferrer me"><span class="invisible">https://</span><span class="">shuuji3.xyz</span><span class="invisible"></span></a>',
                'verified_at': '2022-11-21T03:44:51.983+00:00'},
            {
                'name': 'GitHub',
                'value': '<a href="https://github.com/shuuji3" target="_blank" rel="nofollow noopener noreferrer me"><span class="invisible">https://</span><span class="">github.com/shuuji3</span><span class="invisible"></span></a>',
                'verified_at': '2022-12-19T17:22:50.150+00:00'},
            {
                'name': 'Takahē testing',
                'value': '<a href="https://takahe.social/@shuuji3" target="_blank" rel="nofollow noopener noreferrer me"><span class="invisible">https://</span><span class="">takahe.social/@shuuji3</span><span class="invisible"></span></a>',
                'verified_at': None},
            {
                'name': 'Blog',
                'value': '<a href="https://weblog.shuuji3.xyz" target="_blank" rel="nofollow noopener noreferrer me"><span class="invisible">https://</span><span class="">weblog.shuuji3.xyz</span><span class="invisible"></span></a>',
                'verified_at': None},
        ],
        'role': {
            'id': -99,
            'name': '',
            'permissions': '65536',
            'color': '',
            'highlighted': False,
        },
    }


@pytest.fixture
def twitter_user():
    # api.verify_credentials().__dict__
    yield {
        'id': 1234567,
        'id_str': '1234567',
        'name': 'TAKAHASHI Shuuji',
        'screen_name': 'shuuji3',
        'location': '',
        'description': (
            '<p>🧑🏻\u200d💻 software engineer / 🌟 like: opensource, '
            'technology, science, beautiful things, something fun, '
            'reasonable idea, &amp; fairness</p>'
        ),
        'url': None,
        'entities': {'description': {'urls': []}},
        'protected': False,
        'followers_count': 0,
        'friends_count': 0,
        'listed_count': 0,
        'created_at': datetime.datetime(2023, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc),
        'favourites_count': 0,
        'utc_offset': None,
        'time_zone': None,
        'geo_enabled': False,
        'verified': False,
        'statuses_count': 3,
        'lang': None,
        'status': '''
            Status(_api= < tweepy.api.API object at 0x108c9f880 >, _json = {
                'text': "last tweet text",
                ...
                }
            )
        ''',
        'contributors_enabled': False,
        'is_translator': False,
        'is_translation_enabled': False,
        'profile_background_color': 'F5F8FA',
        'profile_background_image_url': None,
        'profile_background_image_url_https': None,
        'profile_background_tile': False,
        'profile_image_url': 'http://pbs.twimg.com/profile_images/1234567/abcdefg_normal.jpg',
        'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1234567/abcdefg_normal.jpg',
        'profile_link_color': '1DA1F2',
        'profile_sidebar_border_color': 'C0DEED',
        'profile_sidebar_fill_color': 'DDEEF6',
        'profile_text_color': '333333',
        'profile_use_background_image': True,
        'has_extended_profile': True,
        'default_profile': True,
        'default_profile_image': False,
        'following': False,
        'follow_request_sent': False,
        'notifications': False,
        'translator_type': 'none',
        'withheld_in_countries': [],
        'suspended': False,
        'needs_phone_verification': False,
        # '_api': '<tweepy.api.API at 0x108c9f880>',
        # '_json': {
        #     'id': 1234567,
        #     ...
        #     'created_at': 'Fri Jan 01 00:00:00 +0000 2023',
        #     ...
        # },
    }


def test_convert_user(mastodon_api, twitter_user):
    mastodon_user = mastodon_api.me()
    converted_user = convert_user(mastodon_user)
    assert set(converted_user.keys()).issuperset(set(twitter_user.keys()))
