from mastodon import AttribAccessDict
from mastodon.utility import AttribAccessDict

from tweepy_mastodon.models import User


def convert_user(mastodon_account: AttribAccessDict, verified_credentials=False) -> AttribAccessDict:
    mastodon_account['contributors_enabled'] = False  # tentative. what's this?
    mastodon_account['default_profile'] = True  # tentative. what's this?
    mastodon_account['default_profile_image'] = False  # tentative. what's this?
    mastodon_account['description'] = mastodon_account.note
    mastodon_account['entities'] = {'description': {'urls': []}}  # tentative. what's this?
    mastodon_account['favourites_count'] = 0  # no corresponding attribute
    mastodon_account['follow_request_sent'] = mastodon_account.source.follow_requests_count if verified_credentials else 0  # tentative
    mastodon_account['followers_count'] = mastodon_account.followers_count  # tentative
    mastodon_account['following'] = mastodon_account.following_count  # tentative
    mastodon_account['friends_count'] = 0  # no corresponding attribute
    mastodon_account['geo_enabled'] = False  # no corresponding attribute
    mastodon_account['has_extended_profile'] = False  # no corresponding attribute but can be constructed from fields etc.?
    mastodon_account['id'] = mastodon_account.id
    mastodon_account['id_str'] = str(mastodon_account.id)
    mastodon_account['is_translation_enabled'] = False  # no corresponding attribute
    mastodon_account['is_translator'] = False  # no corresponding attribute
    mastodon_account['lang'] = mastodon_account.source.language if verified_credentials else None  # does this have the same format?
    mastodon_account['listed_count'] = 0  # no corresponding attribute
    mastodon_account['location'] = ''  # tentative
    mastodon_account['name'] = mastodon_account.display_name
    mastodon_account['needs_phone_verification'] = False  # no corresponding attribute
    mastodon_account['notifications'] = False  # no corresponding attribute
    mastodon_account['profile_background_color'] = 'F5F8FA'  # tentative
    mastodon_account['profile_background_image_url'] = mastodon_account.header_static
    mastodon_account['profile_background_image_url_https'] = mastodon_account.header_static
    mastodon_account['profile_background_tile'] = False  # tentative
    mastodon_account['profile_image_url'] = mastodon_account.avatar_static
    mastodon_account['profile_image_url_https'] = mastodon_account.avatar_static
    mastodon_account['profile_link_color'] = '1DA1F2'  # tentative
    mastodon_account['profile_sidebar_border_color'] = 'C0DEED'  # tentative
    mastodon_account['profile_sidebar_fill_color'] = 'DDEEF6'  # tentative
    mastodon_account['profile_text_color'] = '333333'  # tentative
    mastodon_account['profile_use_background_image'] = True  # tentative
    mastodon_account['protected'] = mastodon_account.locked
    mastodon_account['screen_name'] = mastodon_account.username
    mastodon_account['status'] = 'TODO'  # TODO: construct Status instance
    mastodon_account['statuses_count'] = mastodon_account.statuses_count
    mastodon_account['suspended'] = False  # tentative
    mastodon_account['time_zone'] = None  # no corresponding attribute
    mastodon_account['translator_type'] = None
    fields = mastodon_account.source.fields if verified_credentials else mastodon_account.fields
    mastodon_account['url'] = fields[0]['value'] if len(fields) > 0 else None
    mastodon_account['utc_offset'] = None  # what's this?
    mastodon_account['verified'] = False  # tentative
    mastodon_account['withheld_in_countries'] = []  # what's this?

    return me
