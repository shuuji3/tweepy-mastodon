from mastodon import Mastodon
from mastodon.utility import AttribAccessDict


def convert_status(
        mastodon_api: Mastodon,
        mastodon_status: AttribAccessDict,
        is_user_embedded=False
) -> AttribAccessDict:
    if not is_user_embedded:
        mastodon_status['author'] = convert_user(mastodon_api, AttribAccessDict(mastodon_status['account']))
    mastodon_status['contributors'] = None
    mastodon_status['coordinates'] = None
    mastodon_status['entities'] = {'hashtags': [], 'symbols': [], 'urls': [], 'user_mentions': []}  # TODO: fill values
    mastodon_status['favorite_count'] = mastodon_status['favourites_count']
    mastodon_status['retweet_count'] = mastodon_status['reblogs_count']
    mastodon_status['favorited'] = mastodon_status['favourited']
    mastodon_status['geo'] = None
    mastodon_status['id'] = mastodon_status['id']
    mastodon_status['id_str'] = str(mastodon_status['id'])
    in_reply_to_account_id = mastodon_status['in_reply_to_account_id']
    if in_reply_to_account_id:
        mastodon_status['in_reply_to_screen_name'] = mastodon_api.account(in_reply_to_account_id).username
    else:
        mastodon_status['in_reply_to_screen_name'] = None
    mastodon_status['in_reply_to_status_id'] = mastodon_status['in_reply_to_id']
    mastodon_status['in_reply_to_status_id_str'] = str(mastodon_status['in_reply_to_id'])
    mastodon_status['in_reply_to_user_id'] = mastodon_status['in_reply_to_account_id']
    mastodon_status['in_reply_to_user_id_str'] = str(mastodon_status['in_reply_to_account_id'])
    mastodon_status['is_quote_status'] = False
    mastodon_status['lang'] = mastodon_status['language']
    mastodon_status['place'] = None
    mastodon_status['retweet_count'] = mastodon_status['reblogs_count']
    mastodon_status['retweeted'] = mastodon_status['reblogged']
    if is_user_embedded:
        if mastodon_status.get('application'):
            application_name = mastodon_status['application']['name']
            application_url = mastodon_status['application']['website']
            mastodon_status['source'] = f'<a href="{application_url}" rel="nofollow">{application_name}</a>'
        else:
            mastodon_status['source'] = None
    else:
        if mastodon_status.get('application'):
            mastodon_status['source'] = mastodon_status['application']['name']
            mastodon_status['source_url'] = mastodon_status['application']['website']
        else:
            mastodon_status['source'] = None
            mastodon_status['source_url'] = None
    mastodon_status['text'] = mastodon_status['content']
    mastodon_status['truncated'] = False
    if not is_user_embedded:
        mastodon_status['user'] = mastodon_status['author']

    return mastodon_status


def convert_user(
        mastodon_api: Mastodon,
        mastodon_account: AttribAccessDict,
        verified_credentials=False,
        get_user=None
) -> AttribAccessDict:
    mastodon_account['contributors_enabled'] = False  # tentative. what's this?
    mastodon_account['default_profile'] = True  # tentative. what's this?
    mastodon_account['default_profile_image'] = False  # tentative. what's this?
    mastodon_account['description'] = mastodon_account.note
    mastodon_account['entities'] = {'description': {'urls': []}}  # tentative. what's this?
    mastodon_account['favourites_count'] = 0  # no corresponding attribute
    if verified_credentials:
        mastodon_account['follow_request_sent'] = mastodon_account.source.follow_requests_count
    else:
        mastodon_account['follow_request_sent'] = 0
    mastodon_account['followers_count'] = mastodon_account.followers_count  # tentative
    mastodon_account['following'] = mastodon_account.following_count  # tentative
    mastodon_account['friends_count'] = 0  # no corresponding attribute
    mastodon_account['geo_enabled'] = False  # no corresponding attribute
    mastodon_account['has_extended_profile'] = False  # no corresponding but can be constructed from fields etc.?
    mastodon_account['id'] = mastodon_account.id
    mastodon_account['id_str'] = str(mastodon_account.id)
    mastodon_account['is_translation_enabled'] = False  # no corresponding attribute
    mastodon_account['is_translator'] = False  # no corresponding attribute
    if verified_credentials:
        mastodon_account['lang'] = mastodon_account.source.language
    else:
        mastodon_account['lang'] = None
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
    mastodon_account['screen_name'] = mastodon_account.acct
    mastodon_account['status'] = convert_status(
        mastodon_api,
        mastodon_api.account_statuses(mastodon_account.id, limit=1)[0],
        is_user_embedded=True
    )
    mastodon_account['statuses_count'] = mastodon_account.statuses_count
    mastodon_account['suspended'] = False  # tentative
    mastodon_account['time_zone'] = None  # no corresponding attribute
    mastodon_account['translator_type'] = 'none'
    if verified_credentials:
        fields = mastodon_account.source.fields
    else:
        fields = mastodon_account.fields
    if len(fields) > 0:
        mastodon_account['url'] = fields[0]['value']
    else:
        mastodon_account['url'] = None
    mastodon_account['utc_offset'] = None  # what's this?
    mastodon_account['verified'] = False  # tentative
    mastodon_account['withheld_in_countries'] = []  # what's this?

    # The `api.get_user()` returns additional field.
    if get_user:
        mastodon_account['profile_location'] = None

    return mastodon_account
