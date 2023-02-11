import logging

from tweepy_mastodon.utils import convert_user, convert_status
from tweepy_mastodon.tweepy.api import API as TweepyAPI

log = logging.getLogger(__name__)

from mastodon import Mastodon, MastodonNotFoundError


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
            log.warning(
                '`trim_user`, `exclude_replies`, and `include_entities` are not implemented in tweepy-mastodon yet')

        mastodon_posts = self.mastodon.timeline_home(limit=count, since_id=since_id, max_id=max_id)
        posts = []
        for mastodon_post in mastodon_posts:
            post = convert_status(self.mastodon, mastodon_post)
            posts.append(post)
        return posts

    # TODO: write argument names explicitly
    def update_status(self, status, **kwargs):
        """update_status( \
            status, *, in_reply_to_status_id, auto_populate_reply_metadata, \
            exclude_reply_user_ids, attachment_url, media_ids, \
            possibly_sensitive, lat, long, place_id, display_coordinates, \
            trim_user, card_uri \
        )

        Updates the authenticating user's current status, also known as
        Tweeting.

        For each update attempt, the update text is compared with the
        authenticating user's recent Tweets. Any attempt that would result in
        duplication will be blocked, resulting in a 403 error. A user cannot
        submit the same status twice in a row.

        While not rate limited by the API, a user is limited in the number of
        Tweets they can create at a time. If the number of updates posted by
        the user reaches the current allowed limit this method will return an
        HTTP 403 error.

        Parameters
        ----------
        status
            The text of your status update.
        in_reply_to_status_id
            The ID of an existing status that the update is in reply to. Note:
            This parameter will be ignored unless the author of the Tweet this
            parameter references is mentioned within the status text.
            Therefore, you must include @username, where username is the author
            of the referenced Tweet, within the update.
        auto_populate_reply_metadata
            If set to true and used with in_reply_to_status_id, leading
            @mentions will be looked up from the original Tweet, and added to
            the new Tweet from there. This wil append @mentions into the
            metadata of an extended Tweet as a reply chain grows, until the
            limit on @mentions is reached. In cases where the original Tweet
            has been deleted, the reply will fail.
        exclude_reply_user_ids
            When used with auto_populate_reply_metadata, a comma-separated list
            of user ids which will be removed from the server-generated
            @mentions prefix on an extended Tweet. Note that the leading
            @mention cannot be removed as it would break the
            in-reply-to-status-id semantics. Attempting to remove it will be
            silently ignored.
        attachment_url
            In order for a URL to not be counted in the status body of an
            extended Tweet, provide a URL as a Tweet attachment. This URL must
            be a Tweet permalink, or Direct Message deep link. Arbitrary,
            non-Twitter URLs must remain in the status text. URLs passed to the
            attachment_url parameter not matching either a Tweet permalink or
            Direct Message deep link will fail at Tweet creation and cause an
            exception.
        media_ids
            A list of media_ids to associate with the Tweet. You may include up
            to 4 photos or 1 animated GIF or 1 video in a Tweet.
        possibly_sensitive
            If you upload Tweet media that might be considered sensitive
            content such as nudity, or medical procedures, you must set this
            value to true.
        lat
            The latitude of the location this Tweet refers to. This parameter
            will be ignored unless it is inside the range -90.0 to +90.0 (North
            is positive) inclusive. It will also be ignored if there is no
            corresponding long parameter.
        long
            The longitude of the location this Tweet refers to. The valid
            ranges for longitude are -180.0 to +180.0 (East is positive)
            inclusive. This parameter will be ignored if outside that range, if
            it is not a number, if geo_enabled is disabled, or if there no
            corresponding lat parameter.
        place_id
            A place in the world.
        display_coordinates
            Whether or not to put a pin on the exact coordinates a Tweet has
            been sent from.
        trim_user
            |trim_user|
        card_uri
            Associate an ads card with the Tweet using the card_uri value from
            any ads card response.

        Returns
        -------
        :class:`~tweepy.models.Status`

        References
        ----------
        https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update
        """
        unimplemented_kwargs = {
            'filename',
            'file',
            'possibly_sensitive',
            'in_reply_to_status_id',
            'lat',
            'long',
            'place_id',
            'display_coordinates',
        }
        if len(unimplemented_kwargs & set(kwargs)) > 0:
            log.warning(f'{unimplemented_kwargs} are not implemented in tweepy-mastodon yet')

        post = self.mastodon.toot(status)
        return convert_status(self.mastodon, post)

    def get_user(self, user_id=None, screen_name=None, include_entities=None):
        """get_user(*, user_id, screen_name, include_entities)

        Returns information about the specified user.

        Parameters
        ----------
        user_id
            |user_id|
        screen_name
            |screen_name|
        include_entities
            |include_entities|

        Returns
        -------
        :class:`~tweepy.models.User`

        References
        ----------
        https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-show
        """
        if include_entities is not None:
            log.warning('`include_entities` is not implemented in tweepy-mastodon yet')

        try:
            if user_id:
                user = self.mastodon.account(id=user_id)
            elif screen_name:
                user = self.mastodon.account_lookup(acct=screen_name)
            else:
                raise Exception('404 not found')  # TODO: use actual `tweepy.errors.NotFound`
        except MastodonNotFoundError:
            raise Exception('404 not found')  # TODO: use actual `tweepy.errors.NotFound`

        return convert_user(self.mastodon, user, get_user=True)

    def user_timeline(
            self,
            user_id=None,
            screen_name=None,
            since_id=None,
            count=None,
            max_id=None,
            trim_user=None,
            exclude_replies=None,
            include_rts=None
    ):
        """user_timeline(*, user_id, screen_name, since_id, count, max_id,
                        trim_user, exclude_replies, include_rts)

        Returns the 20 most recent statuses posted from the authenticating user
        or the user specified. It's also possible to request another user's
        timeline via the id parameter.

        Parameters
        ----------
        user_id
            |user_id|
        screen_name
            |screen_name|
        since_id
            |since_id|
        count
            |count|
        max_id
            |max_id|
        trim_user
            |trim_user|
        exclude_replies
            |exclude_replies|
        include_rts
            When set to ``false``, the timeline will strip any native retweets
            (though they will still count toward both the maximal length of the
            timeline and the slice selected by the count parameter). Note: If
            you're using the trim_user parameter in conjunction with
            include_rts, the retweets will still contain a full user object.

        Returns
        -------
        :py:class:`List`\[:class:`~tweepy.models.Status`]

        References
        ----------
        https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline
        """
        if trim_user is not None or exclude_replies is not None or include_rts is not None:
            log.warning(
                '`trim_user`, `exclude_replies`, and `include_rts` are not implemented in tweepy-mastodon yet')

        mastodon_posts = self.mastodon.timeline_home(limit=count, since_id=since_id, max_id=max_id)
        posts = []
        for mastodon_post in mastodon_posts:
            post = convert_status(self.mastodon, mastodon_post)
            posts.append(post)
        return posts

    def get_status(
            self,
            id,
            trim_user=None,
            include_my_retweet=None,
            include_entities=None,
            include_ext_alt_text=None,
            include_card_uri=None
    ):
        """get_status(id, *, trim_user, include_my_retweet, include_entities, \
                      include_ext_alt_text, include_card_uri)

        Returns a single status specified by the ID parameter.

        Parameters
        ----------
        id:
            |sid|
        trim_user
            |trim_user|
        include_my_retweet:
            A boolean indicating if any Tweets returned that have been
            retweeted by the authenticating user should include an additional
            current_user_retweet node, containing the ID of the source status
            for the retweet.
        include_entities
            |include_entities|
        include_ext_alt_text
            |include_ext_alt_text|
        include_card_uri
            |include_card_uri|

        Returns
        -------
        :class:`~tweepy.models.Status`

        References
        ----------
        https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-show-id
        """

        if trim_user is not None \
                or include_my_retweet is not None \
                or include_entities is not None \
                or include_ext_alt_text is not None \
                or include_card_uri is not None:
            log.warning(
                '`trim_user`, `include_my_retweet`, `include_entities`, `include_ext_alt_text`, '
                'and `include_card_uri` are not implemented in tweepy-mastodon yet')

        status = self.mastodon.status(id=id)
        return convert_status(self.mastodon, status, include_user_status=False)

    def create_favorite(self, id, include_entities=None):
        """create_favorite(id, *, include_entities)

        Favorites the status specified in the ``id`` parameter as the
        authenticating user.

        Parameters
        ----------
        id
            |sid|
        include_entities
            |include_entities|

        Returns
        -------
        :class:`~tweepy.models.Status`

        References
        ----------
        https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-create
        """

        if include_entities is not None:
            log.warning('`include_entities` are not implemented in tweepy-mastodon yet')

        try:
            mastodon_status = self.mastodon.status_favourite(id=id)
            return convert_status(self.mastodon, mastodon_status, include_user_status=False)
        except MastodonNotFoundError:
            raise Exception('404 not found')  # TODO: use actual `tweepy.errors.NotFound`

    def destroy_favorite(self, id, include_entities=None):
        """destroy_favorite(id, *, include_entities)

        Un-favorites the status specified in the ``id`` parameter as the
        authenticating user.

        Parameters
        ----------
        id
            |sid|
        include_entities
            |include_entities|

        Returns
        -------
        :class:`~tweepy.models.Status`

        References
        ----------
        https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-destroy
        """
        if include_entities is not None:
            log.warning('`include_entities` are not implemented in tweepy-mastodon yet')

        try:
            mastodon_status = self.mastodon.status_unfavourite(id=id)
            return convert_status(self.mastodon, mastodon_status, include_user_status=False)
        except MastodonNotFoundError:
            raise Exception('404 not found')  # TODO: use actual `tweepy.errors.NotFound`

    def retweet(self, id, trim_user=None):
        """retweet(id, *, trim_user)

        Retweets a Tweet. Requires the ID of the Tweet you are retweeting.

        Parameters
        ----------
        id
            |sid|
        trim_user
            |trim_user|

        Returns
        -------
        :class:`~tweepy.models.Status`

        References
        ----------
        https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-retweet-id
        """

        if trim_user is not None:
            log.warning('`trim_user` are not implemented in tweepy-mastodon yet')

        try:
            mastodon_status = self.mastodon.status_reblog(id=id)
            return convert_status(self.mastodon, mastodon_status, include_user_status=False)
        except MastodonNotFoundError:
            raise Exception('404 not found')  # TODO: use actual `tweepy.errors.NotFound`

    def unretweet(self, id, trim_user=None):
        """unretweet(id, *, trim_user)

        Untweets a retweeted status. Requires the ID of the retweet to
        unretweet.

        Parameters
        ----------
        id
            |sid|
        trim_user
            |trim_user|

        Returns
        -------
        :class:`~tweepy.models.Status`

        References
        ----------
        https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-unretweet-id
        """
        if trim_user is not None:
            log.warning('`trim_user` are not implemented in tweepy-mastodon yet')

        try:
            mastodon_status = self.mastodon.status_unreblog(id=id)
            return convert_status(self.mastodon, mastodon_status, include_user_status=False)
        except MastodonNotFoundError:
            raise Exception('404 not found')  # TODO: use actual `tweepy.errors.NotFound`

    def create_friendship(self, screen_name=None, user_id=None, follow=False):
        """create_friendship(*, screen_name, user_id, follow)

        Create a new friendship with the specified user (aka follow).

        Parameters
        ----------
        screen_name
            |screen_name|
        user_id
            |user_id|
        follow
            Enable notifications for the target user in addition to becoming
            friends.

        Returns
        -------
        :class:`~tweepy.models.User`

        References
        ----------
        https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-create
        """
        try:
            user = self.get_user(user_id, screen_name)
            relationship = self.mastodon.account_follow(id=user.id, notify=follow)

            user['following'] = relationship.following
            user['notifications'] = relationship.notifying
            user['follow_request_sent'] = relationship.requested

            return user
        except MastodonNotFoundError:
            raise Exception('404 not found')  # TODO: use actual `tweepy.errors.NotFound`


    def destroy_friendship(self, screen_name=None, user_id=None):
        """destroy_friendship(*, screen_name, user_id)

        Destroy a friendship with the specified user (aka unfollow).

        Parameters
        ----------
        screen_name
            |screen_name|
        user_id
            |user_id|

        Returns
        -------
        :class:`~tweepy.models.User`

        References
        ----------
        https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-destroy
        """
        try:
            user: User = self.get_user(user_id, screen_name)
            relationship = self.mastodon.account_unfollow(id=user.id)

            user['following'] = relationship.following
            user['notifications'] = relationship.notifying
            user['follow_request_sent'] = relationship.requested

            return user
        except MastodonNotFoundError:
            raise Exception('404 not found')  # TODO: use actual `tweepy.errors.NotFound`

