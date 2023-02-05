import logging

from tweepy_mastodon.utils import convert_user, convert_status
from tweepy_mastodon.tweepy.api import API as TweepyAPI

log = logging.getLogger(__name__)

from mastodon import Mastodon


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

        if auth is not None:
            self.mastodon = Mastodon(
                auth.client_id,
                auth.client_secret,
                auth.access_token,
                api_base_url=auth.api_base_url,
            )

    def verify_credentials(self, **kwargs):
        me = self.mastodon.me()
        return convert_user(self.mastodon, me, verified_credentials=True)

    def home_timeline(
            self,
            count=20,
            since_id=None,
            max_id=None,
            trim_user=None,
            exclude_replies=None,
            include_entities=None,
            **kwargs
    ):
        """home_timeline(*, count, since_id, max_id, trim_user, exclude_replies, include_entities)

        Returns the 20 most recent statuses, including retweets, posted by
        the authenticating user and that user's friends. This is the equivalent
        of /timeline/home on the Web.

        Parameters
        ----------
        count
            |count|
        since_id
            |since_id|
        max_id
            |max_id|
        trim_user
            |trim_user|
        exclude_replies
            |exclude_replies|
        include_entities
            |include_entities|

        Returns
        -------
        :py:class:`List`\[:class:`~tweepy.models.Status`]

        References
        ----------
        https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-home_timeline
        """
        if trim_user is not None or exclude_replies is not None or include_entities is not None:
            log.warning('`trim_user`, `exclude_replies`, and `include_entities` are not implemented in tweepy-mastodon yet')

        mastodon_posts = self.mastodon.timeline_home(limit=count, since_id=since_id, max_id=max_id)
        posts = []
        for mastodon_post in mastodon_posts:
            post = convert_status(self.mastodon, mastodon_post)
            posts.append(post)
        return posts
