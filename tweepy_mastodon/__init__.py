# Tweepy
# Copyright 2009-2023 Joshua Roesslein
# See LICENSE for details.

"""
Tweepy Twitter API library
"""
__version__ = '0.1.0'
__author__ = 'TAKAHASHI Shuuji'
__license__ = 'MIT'

from tweepy_mastodon.api import API
from tweepy_mastodon.auth import OAuth1UserHandler
from tweepy_mastodon.tweepy.auth import (
    AppAuthHandler, OAuthHandler, OAuth2AppHandler,
    OAuth2BearerHandler, OAuth2UserHandler
)
from tweepy_mastodon.cache import Cache, FileCache, MemoryCache
from tweepy_mastodon.client import Client, Response
from tweepy_mastodon.cursor import Cursor
from tweepy_mastodon.direct_message_event import DirectMessageEvent
from tweepy_mastodon.errors import (
    BadRequest, Forbidden, HTTPException, NotFound, TooManyRequests,
    TweepyException, TwitterServerError, Unauthorized
)
from tweepy_mastodon.list import List
from tweepy_mastodon.media import Media
from tweepy_mastodon.pagination import Paginator
from tweepy_mastodon.place import Place
from tweepy_mastodon.poll import Poll
from tweepy_mastodon.space import Space
from tweepy_mastodon.streaming import (
    Stream, StreamingClient, StreamResponse, StreamRule
)
from tweepy_mastodon.tweet import ReferencedTweet, Tweet
from tweepy_mastodon.user import User

# Global, unauthenticated instance of API
api = API()
