import logging

from tweepy_mastodon.utils import convert_user
from tweepy_mastodon.tweepy.api import API as TweepyAPI

log = logging.getLogger(__name__)

from mastodon import Mastodon
import os
import sys


def mastodon_api() -> Mastodon:
    api_base_url = os.environ.get('MASTODON_API_BASE_URL')
    client_id = os.environ.get('MASTODON_CLIENT_ID')
    client_secret = os.environ.get('MASTODON_CLIENT_SECRET')
    access_token = os.environ.get('MASTODON_ACCESS_TOKEN')

    if not (client_id and client_secret and access_token):
        print('environment variable not found!')
        sys.exit(1)

    return Mastodon(client_id, client_secret, access_token, api_base_url=api_base_url)


class API(TweepyAPI):
    """Twitter API v1.1 Interface

    .. versionchanged:: 4.11
        Added support for ``include_ext_edit_control`` endpoint/method
        parameter

    Parameters
    ----------
    auth
        The authentication handler to be used
    cache
        The cache to query if a GET method is used
    host
        The general REST API host server URL
    parser
        The Parser instance to use for parsing the response from Twitter;
        defaults to an instance of ModelParser
    proxy
        The full url to an HTTPS proxy to use for connecting to Twitter
    retry_count
        Number of retries to attempt when an error occurs
    retry_delay
        Number of seconds to wait between retries
    retry_errors
        Which HTTP status codes to retry
    timeout
        The maximum amount of time to wait for a response from Twitter
    upload_host
        The URL of the upload server
    wait_on_rate_limit
        Whether or not to automatically wait for rate limits to replenish

    Raises
    ------
    TypeError
        If the given parser is not a Parser instance

    References
    ----------
    https://developer.twitter.com/en/docs/api-reference-index
    """

    def __init__(
            self, auth=None, *, cache=None, host='api.twitter.com', parser=None,
            proxy=None, retry_count=0, retry_delay=0, retry_errors=None,
            timeout=60, upload_host='upload.twitter.com', user_agent=None,
            wait_on_rate_limit=False
    ):
        super().__init__(
            auth, cache=cache, host=host, parser=parser, proxy=proxy, retry_count=retry_count,
            retry_delay=retry_delay, retry_errors=retry_errors, timeout=timeout, upload_host=upload_host,
            user_agent=user_agent, wait_on_rate_limit=wait_on_rate_limit
        )
        self.mastodon = mastodon_api()

    def verify_credentials(self, **kwargs):
        me = self.mastodon.me()
        return convert_user(me)
