from mastodon import AttribAccessDict
from mastodon.utility import AttribAccessDict

from tweepy_mastodon.models import User


def convert_user(me: AttribAccessDict) -> AttribAccessDict:
    me['contributors_enabled'] = False  # tentative. what's this?
    me['default_profile'] = True  # tentative. what's this?
    me['default_profile_image'] = False  # tentative. what's this?
    me['description'] = me.note
    me['entities'] = {'description': {'urls': []}}  # tentative. what's this?
    me['favourites_count'] = 0  # no corresponding attribute
    me['follow_request_sent'] = me.source.follow_requests_count  # tentative
    me['followers_count'] = me.followers_count  # tentative
    me['following'] = me.following_count  # tentative
    me['friends_count'] = 0  # no corresponding attribute
    me['geo_enabled'] = False  # no corresponding attribute
    me[
        'has_extended_profile'] = False  # no corresponding attribute but can be constructed from metadata fields etc.?
    me['id'] = me.id
    me['id_str'] = str(me.id)
    me['is_translation_enabled'] = False  # no corresponding attribute
    me['is_translator'] = False  # no corresponding attribute
    me['lang'] = me.source.language  # does this have the same format?
    me['listed_count'] = 0  # no corresponding attribute
    me['location'] = ''  # tentative
    me['name'] = me.display_name
    me['needs_phone_verification'] = False  # no corresponding attribute
    me['notifications'] = False  # no corresponding attribute
    me['profile_background_color'] = 'F5F8FA'  # tentative
    me['profile_background_image_url'] = me.header_static
    me['profile_background_image_url_https'] = me.header_static
    me['profile_background_tile'] = False  # tentative
    me['profile_image_url'] = me.avatar_static
    me['profile_image_url_https'] = me.avatar_static
    me['profile_link_color'] = '1DA1F2'  # tentative
    me['profile_sidebar_border_color'] = 'C0DEED'  # tentative
    me['profile_sidebar_fill_color'] = 'DDEEF6'  # tentative
    me['profile_text_color'] = '333333'  # tentative
    me['profile_use_background_image'] = True  # tentative
    me['protected'] = me.locked
    me['screen_name'] = me.username
    me['status'] = 'TODO'  # TODO: construct Status instance
    me['statuses_count'] = me.statuses_count
    me['suspended'] = False  # tentative
    me['time_zone'] = None  # no corresponding attribute
    me['translator_type'] = None
    me['url'] = me.source.fields[0].value if len(me.source.fields) > 0 else None
    me['utc_offset'] = None  # what's this?
    me['verified'] = False  # tentative
    me['withheld_in_countries'] = []  # what's this?

    return me
