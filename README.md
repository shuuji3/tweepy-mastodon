# 🐘 tweepy-mastodon: [experimental] Mastodon API library with Tweepy interface for Python

[![PyPI Version](https://img.shields.io/pypi/v/tweepy-mastodon?label=PyPI)](https://pypi.org/project/tweepy/)
[![Python Versions](https://img.shields.io/pypi/pyversions/tweepy?label=Python)](https://pypi.org/project/tweepy/)
 
[![Twitter API v1.1](https://img.shields.io/endpoint?url=https%3A%2F%2Ftwbadges.glitch.me%2Fbadges%2Fstandard)](https://developer.twitter.com/en/docs/twitter-api/v1)<!-- [![Twitter API v2](https://img.shields.io/endpoint?url=https%3A%2F%2Ftwbadges.glitch.me%2Fbadges%2Fv2)](https://developer.twitter.com/en/docs/twitter-api) -->
[![Documentation Status](https://readthedocs.org/projects/tweepy-mastodon/badge/?version=latest)](https://tweepy-mastodon.readthedocs.io/en/latest/)
[![Test Status](https://github.com/shuuji3/tweepy-mastodon/workflows/Test/badge.svg)](https://github.com/shuuji3/tweepy-mastodon/actions?query=workflow%3ATest)
[![Coverage Status](https://img.shields.io/coveralls/shuuji3/tweepy-mastodon/mastodon.svg?style=flat)](https://coveralls.io/github/shuuji3/tweepy-mastodon?branch=mastodon)

![cherry blossom photo](https://files.mastodon.social/accounts/headers/000/936/436/original/4d6989a698953e80.jpg)

> ⚠ This library is under development! Only partial features are implemented.

An attempt to provide Mastodon API library with Tweepy-like interface, to help developers to migrate their good bot/service built with Tweepy to Mastodon easily.

## Implemented API

| API | Implemented? | Note |
| --- | -- | -- |
| `tweepy.OAuth1UserHandler` <br> (previously `tweepy.OAuthHandler` ) | ✅ |  |
| `api.verify_credentials()` | ✅ |  |
| `api.update_status()` | ✅ | partially |
| `api.home_timeline()` | ✅ | partially |
| `api.get_user()` | ✅ | partially |
| `api.user_timeline()` | 📝 TODO |  |
| `api.get_status()` | 📝 TODO |  |
| `api.update_status_with_media()` | 📝 TODO |  |
| `api.create_favorite()` | 📝 TODO |  |
| `api.retweet()` | 📝 TODO |  |
| `api.create_friendship()` <br> (a.k.a. follow) | 📝 TODO |  |
| ... | 📝 TODO |  |
| `api.mastodon` | ✅ | Bonus: You can use any Mastodon.py API ✨ |

## Example usage

Please prepare your Mastodon API credentials from the developer settings page (example URL: https://mastodon.social/settings/applications).

```py
import datetime

import tweepy_mastodon as tweepy

api_base_url = 'mastodon.social'
mastodon_client_id = 'xxxxxxx'
mastodon_client_secret = 'xxxxxxx'
mastodon_access_token = 'xxxxxxx'

auth = tweepy.OAuth1UserHandler(
    consumer_key=mastodon_client_id,
    consumer_secret=mastodon_client_secret,
    api_base_url=api_base_url
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

assert me.favorited == False
assert me.retweeted == False
assert me.status.source == '<a href="https://elk.zone" rel="nofollow">Elk</a>'

user = api.get_user(user_id=1)
assert user.id_str == '1'
assert user.screen_name == 'Gargron'
assert user.name == 'Eugen Rochko'

user = api.get_user(screen_name='npr@mstdn.social')
assert user.id == 1201325
assert user.screen_name == 'NPR@mstdn.social'
assert user.name == 'NPR :verified:'
```

## Installation

> TODO: Not published to PyPI yet!

The easiest way to install the latest version from PyPI is by using
[pip](https://pip.pypa.io/):

    pip install tweepy-mastodon

To use the `tweepy.asynchronous` subpackage, be sure to install with the
`async` extra:

    pip install tweepy-mastodon[async]

You can also use Git to clone the repository from GitHub to install the latest
development version:

    git clone https://github.com/shuuji3/tweepy-mastodon.git
    cd tweepy-mastodon
    pip install .

Alternatively, install directly from the GitHub repository:

    pip install git+https://github.com/shuuji3/tweepy-mastodon.git

Python 3.7 - 3.11 are supported.

Links
-----

- [Documentation](https://tweepy-mastodon.readthedocs.io/en/latest/)
- [halcy/Mastodon.py: Python wrapper for the Mastodon API](https://github.com/halcy/Mastodon.py/)
- [Twitter API Documentation](https://developer.twitter.com/en/docs/twitter-api)
