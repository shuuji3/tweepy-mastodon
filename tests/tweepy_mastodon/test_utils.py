import datetime
from dateutil.tz import tzutc

from mastodon.utility import AttribAccessDict
import pytest

from tests.tweepy_mastodon.test_api import mastodon_api
from tweepy_mastodon.utils import convert_user, convert_status


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
def twitter_verify_credentials(twitter_user):
    # api.verify_credentials().__dict__
    del twitter_user['profile_location']
    twitter_user['suspended'] = False
    twitter_user['needs_phone_verification'] = False
    return twitter_user


@pytest.fixture
def twitter_user():
    # api.get_user.__dict__
    yield {
        'id': 1234567,
        'id_str': '1234567',
        'name': 'TAKAHASHI Shuuji',
        'screen_name': 'shuuji3',
        'location': '',
        'profile_location': None,
        'description': (
            '<p>🧑🏻\u200d💻 software engineer / 🌟 like: opensource, '
            'technology, science, beautiful things, something fun, '
            'reasonable idea, &amp; fairness</p>'
        ),
        'url': None,
        'entities': {
            'description': {'urls': []},
            'url': {
                'urls': [
                    {
                        'url': 'https://t.co/Wriee1u6Um',
                        'expanded_url': 'https://github.com/sakuramochi0/kinpri-goods-wiki',
                        'display_url': 'github.com/sakuramochi0/k…',
                        'indices': [0, 23]
                    }
                ]
            }
        },
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
        # '_api': '<tweepy.api.API at 0x108c9f880>',
        # '_json': {
        #     'id': 1234567,
        #     ...
        #     'created_at': 'Fri Jan 01 00:00:00 +0000 2023',
        #     ...
        # },
    }


@pytest.fixture
def twitter_status():
    yield {
        'created_at': datetime.datetime(2023, 2, 3, 16, 45, tzinfo=datetime.timezone.utc),
        'id': 109801812845135807,
        'id_str': '109801812845135807',
        'text': 'tweet test example',
        'truncated': False,
        'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': []},
        'source': 'Twitter Web App',
        'source_url': 'https://mobile.twitter.com',
        'in_reply_to_status_id': None,
        'in_reply_to_status_id_str': None,
        'in_reply_to_user_id': None,
        'in_reply_to_user_id_str': None,
        'in_reply_to_screen_name': None,
        'author': '''User(_api=<tweepy.api.API object at 0x10acff220>, 'text': 'example tweet text'...''',
        'user': '''User(_api=<tweepy.api.API object at 0x10acff220>, 'text': 'example tweet text'...''',
        'geo': None,
        'coordinates': None,
        'place': None,
        'contributors': None,
        'is_quote_status': False,
        'retweet_count': 0,
        'favorite_count': 0,
        'favorited': False,
        'retweeted': False,
        'lang': 'in'
    }


@pytest.fixture
def mastodon_status():
    yield AttribAccessDict({
        'id': 109801812845135807,
        'created_at': datetime.datetime(2023, 2, 3, 16, 45, 0, 892000, tzinfo=tzutc()),
        'in_reply_to_id': 109801363905285407,
        'in_reply_to_account_id': 936436,
        'sensitive': False,
        'spoiler_text': '',
        'visibility': 'public',
        'language': 'en',
        'uri': 'https://mastodon.social/users/shuuji3/statuses/109801812845135807',
        'url': 'https://mastodon.social/@shuuji3/109801812845135807',
        'replies_count': 0,
        'reblogs_count': 0,
        'favourites_count': 0,
        'edited_at': None,
        'favourited': False,
        'reblogged': False,
        'muted': False,
        'bookmarked': False,
        'pinned': False,
        'content': '<p>There&#39;s the previous attempt to implement a Tweepy-like library to talk with Mastodon API called &quot;pawopy&quot;. But it was archived 5 years ago: <a href="https://github.com/calmery/Pawopy" target="_blank" rel="nofollow noopener noreferrer"><span class="invisible">https://</span><span class="">github.com/calmery/Pawopy</span><span class="invisible"></span></a></p>',
        'filtered': [],
        'reblog': None,
        'application': {'name': 'Elk', 'website': 'https://elk.zone'},
        'account': {
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
            'emojis': [],
            'fields': [
                {
                    'name': 'Website',
                    'value': '<a href="https://shuuji3.xyz" target="_blank" rel="nofollow noopener noreferrer me"><span class="invisible">https://</span><span class="">shuuji3.xyz</span><span class="invisible"></span></a>',
                    'verified_at': '2022-11-21T03:44:51.983+00:00'
                },
                {
                    'name': 'GitHub',
                    'value': '<a href="https://github.com/shuuji3" target="_blank" rel="nofollow noopener noreferrer me"><span class="invisible">https://</span><span class="">github.com/shuuji3</span><span class="invisible"></span></a>',
                    'verified_at': '2022-12-19T17:22:50.150+00:00'
                },
                {
                    'name': 'Takahē testing',
                    'value': '<a href="https://takahe.social/@shuuji3" target="_blank" rel="nofollow noopener noreferrer me"><span class="invisible">https://</span><span class="">takahe.social/@shuuji3</span><span class="invisible"></span></a>',
                    'verified_at': None
                },
                {
                    'name': 'Blog',
                    'value': '<a href="https://weblog.shuuji3.xyz" target="_blank" rel="nofollow noopener noreferrer me"><span class="invisible">https://</span><span class="">weblog.shuuji3.xyz</span><span class="invisible"></span></a>',
                    'verified_at': None
                }
            ]
        },
        'media_attachments': [],
        'mentions': [],
        'tags': [],
        'emojis': [],
        'card': {
            'url': 'https://github.com/calmery/Pawopy',
            'title': 'GitHub - calmery/Pawopy: A Python wrapper for the Mastodon API like tweepy',
            'description': 'A Python wrapper for the Mastodon API like tweepy. Contribute to calmery/Pawopy development by creating an account on GitHub.',
            'type': 'link',
            'author_name': '',
            'author_url': '',
            'provider_name': 'GitHub',
            'provider_url': '',
            'html': '',
            'width': 400,
            'height': 200,
            'image': 'https://files.mastodon.social/cache/preview_cards/images/053/803/844/original/64ace706daf69a5e.png',
            'embed_url': '',
            'blurhash': 'UOS6Sut7fQt7%1ofj[ofE2Rjofj[~pRjj[WB'
        },
        'poll': None,
    })


def test_convert_user_verifiy_credentials(mastodon_api, twitter_verify_credentials):
    mastodon_user = mastodon_api.me()
    converted_user = convert_user(mastodon_api, mastodon_user, verified_credentials=True)
    assert set(converted_user.keys()).issuperset(set(twitter_verify_credentials.keys()))

    # Enable only during development since the mastodon data structure has extra properties and not exactly the same
    # assert converted_user == twitter_verify_credentials


def test_convert_user(mastodon_api, twitter_user):
    mastodon_user = mastodon_api.me()
    converted_user = convert_user(mastodon_api, mastodon_user, verified_credentials=False, get_user=True)
    print(twitter_user.keys() - converted_user.keys())
    assert set(converted_user.keys()).issuperset(set(twitter_user.keys()))

    # Enable only during development since the mastodon data structure has extra properties and not exactly the same
    # assert converted_user == twitter_user


def test_convert_status(mastodon_api, mastodon_status, twitter_status):
    converted_status = convert_status(mastodon_api, mastodon_status)
    assert set(converted_status.keys()).issuperset(set(twitter_status.keys()))

    # Enable only during development since the mastodon data structure has extra properties and not exactly the same
    # assert converted_status == twitter_status
