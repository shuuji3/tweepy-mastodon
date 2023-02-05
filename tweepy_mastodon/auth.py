from tweepy_mastodon.tweepy.auth import OAuth1UserHandler as TweepyOAuth1UserHandler


class OAuth1UserHandler(TweepyOAuth1UserHandler):
    """
    OAuth 1.0a User Context authentication handler.

    The tweepy-mastodon library does not use `access_token_secret` since Mastodon.py requires only three credentials:
    client_id (consumer_key), client_secret (consumer_secret), and access_token.
    """

    def __init__(
            self, consumer_key, consumer_secret, access_token=None,
            access_token_secret=None, callback=None, api_base_url=None
    ):
        if api_base_url is None:
            raise Exception(
                'tweepy-mastodon requires the additional parameter `api_base_url` to determine Mastodon API server'
            )

        access_token_secret = None
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret, callback)

        self.api_base_url = api_base_url

    @property
    def client_id(self):
        """Alias of `consumer_key` for Mastodon API."""
        return self.consumer_key

    @property
    def client_secret(self):
        """Alias of `consumer_secret` for Mastodon API."""
        return self.consumer_secret

    def set_access_token(self, key, secret=None):
        super().set_access_token(key, None)
