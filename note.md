## test api.toot(text: str)

```py
api.mastodon.toot('test toot from normal Mastodon API 🐘')

{
    'id': 109813449400616131,
    'created_at': datetime.datetime(2023, 2, 5, 18, 4, 20, 638000, tzinfo=tzutc()),
    'in_reply_to_id': None,
    'in_reply_to_account_id': None,
    'sensitive': False,
    'spoiler_text': '',
    'visibility': 'public',
    'language': 'ja',
    'uri': 'https://mastodon.social/users/shuuji3/statuses/109813449400616131',
    'url': 'https://mastodon.social/@shuuji3/109813449400616131',
    'replies_count': 0,
    'reblogs_count': 0,
    'favourites_count': 0,
    'edited_at': None,
    'favourited': False,
    'reblogged': False,
    'muted': False,
    'bookmarked': False,
    'pinned': False,
    'content': '<p>test toot from normal Mastodon API 🐘</p>',
    'filtered': [],
    'reblog': None,
    'application': {
        'name': 'tweepy-mastodon',
        'website': 'https://github.com/shuuji3/tweepy-mastodon',
    },
    'account': {
        'id': 936436,
        'username': 'shuuji3',
        'acct': 'shuuji3',
        'display_name': 'TAKAHASHI Shuuji 🌈✨',
        'locked': False,
        'bot': False,
        'discoverable': False,
        'group': False,
        'created_at': datetime.datetime(2019, 10, 8, 0, 0, tzinfo=tzutc()),
        'note': '<p>🧑🏻\u200d💻 software engineer / 🌟 like: opensource, technology, science, beautiful things, something fun, reasonable idea, &amp; fairness</p>',
        'url': 'https://mastodon.social/@shuuji3',
        'avatar': 'https://files.mastodon.social/accounts/avatars/000/936/436/original/4854d6cf9e12cb8f.png',
        'avatar_static': 'https://files.mastodon.social/accounts/avatars/000/936/436/original/4854d6cf9e12cb8f.png',
        'header': 'https://files.mastodon.social/accounts/headers/000/936/436/original/4d6989a698953e80.jpg',
        'header_static': 'https://files.mastodon.social/accounts/headers/000/936/436/original/4d6989a698953e80.jpg',
        'followers_count': 18,
        'following_count': 35,
        'statuses_count': 80,
        'last_status_at': datetime.datetime(2023, 2, 5, 0, 0),
        'noindex': False,
        'emojis': [],
        'fields': [
            {
                'name': 'Website',
                'value': '<a href="https://shuuji3.xyz" target="_blank" rel="nofollow noopener noreferrer me"><span class="invisible">https://</span><span class="">shuuji3.xyz</span><span class="invisible"></span></a>',
                'verified_at': '2022-11-21T03:44:51.983+00:00',
            },
            {
                'name': 'GitHub',
                'value': '<a href="https://github.com/shuuji3" target="_blank" rel="nofollow noopener noreferrer me"><span class="invisible">https://</span><span class="">github.com/shuuji3</span><span class="invisible"></span></a>',
                'verified_at': '2022-12-19T17:22:50.150+00:00',
            },
            {
                'name': 'Takahē testing',
                'value': '<a href="https://takahe.social/@shuuji3" target="_blank" rel="nofollow noopener noreferrer me"><span class="invisible">https://</span><span class="">takahe.social/@shuuji3</span><span class="invisible"></span></a>',
                'verified_at': None,
            },
            {
                'name': 'Blog',
                'value': '<a href="https://weblog.shuuji3.xyz" target="_blank" rel="nofollow noopener noreferrer me"><span class="invisible">https://</span><span class="">weblog.shuuji3.xyz</span><span class="invisible"></span></a>',
                'verified_at': None,
            }
        ]
    },
    'media_attachments': [],
    'mentions': [],
    'tags': [],
    'emojis': [],
    'card': None,
    'poll': None,
}
```
