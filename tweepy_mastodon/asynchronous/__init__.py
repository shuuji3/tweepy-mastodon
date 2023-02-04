# Tweepy
# Copyright 2009-2023 Joshua Roesslein
# See LICENSE for details.

"""
Tweepy.asynchronoous

Asynchronous interfaces with the Twitter API
"""

try:
    import aiohttp
    import async_lru
    import oauthlib
except ModuleNotFoundError:
    from tweepy_mastodon.errors import TweepyException
    raise TweepyException(
        "tweepy.asynchronous requires aiohttp, async_lru, and oauthlib to be "
        "installed"
    )

from tweepy_mastodon.asynchronous.client import AsyncClient
from tweepy_mastodon.asynchronous.pagination import AsyncPaginator
from tweepy_mastodon.asynchronous.streaming import AsyncStream, AsyncStreamingClient
