AUTHOR = u'Marco Chomut'
SITENAME = u'Marco\'s Modern Life'
SITEURL = 'http://marcosmodernlife.com'
TIMEZONE = "America/New_York"

OUTPUT_PATH = '../bin/'
ARTICLE_PERMALINK_STRUCTURE = '/blog/%Y/%m/%d/'
GITHUB_URL = 'http://github.com/Pewpewarrows/'
DISQUS_SITENAME = 'mymodernlife'
PDF_GENERATOR = False
REVERSE_ARCHIVE_ORDER = True
REVERSE_CATEGORY_ORDER = True
LOCALE = ''
DEFAULT_PAGINATION = 5

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_RSS = 'feeds/tag_%s.rss.xml'
FEED_MAX_ITEMS = 100

LINKS = (
    ('Google', 'http://google.com'),
)

SOCIAL = (
    ('twitter', 'http://twitter.com/pewpewarrows'),
    ('github', 'http://github.com/Pewpewarrows'),
)

GOOGLE_ANALYTICS = ''
TWITTER_USERNAME = 'pewpewarrows'
MENUITEMS = ()

# global metadata to all the contents
DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
# THEME_STATIC_PATHS
# STATIC_PATHS = [
#     '../res/static'
# ]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (
    ('../res/static/robots.txt', 'robots.txt'),
    ('../res/static/humans.txt', 'humans.txt'),
    ('../res/static/favicon.ico', 'favicon.ico'),
    ('../res/CNAME', 'CNAME'),
)